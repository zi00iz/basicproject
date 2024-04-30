import os
import math
import uvicorn
import requests, json
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import pymongo
from pymongo import MongoClient
import pymysql
from pydantic import BaseModel
from typing import Optional
from database import dbConn

# Mongodb 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
secret_file = os.path.join(BASE_DIR, 'secret.json')

# secret 파일 읽어오기
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("Mongo_Hostname")
USERNAME = get_secret("Mongo_Username")
PASSWORD = get_secret("Mongo_Password")

client = MongoClient(f'mongodb://{USERNAME}:{PASSWORD}@{HOSTNAME}' )
print ('Connected to Mongodb ... ')

mymon = client['bikeproject']
mycolbus = mymon['buspath']
mycolsub = mymon['subwaypath']

app = FastAPI()
db = dbConn()

    
#savesql : jiwon에게 최적화 기록(sqlData)받기
@app.post("/saveSql")
async def save_sql(data:dict):  #(SearchId, Sx, Sy, Ex, Ey, STotalTime, STotalDistance, BTotalTime, BTotalDistance, Optipath, Diff)
    values = tuple(data.values())
    try:
        db.connect()  # 데이터베이스 연결
        cursor = db.get_cursor()  # 커서 가져오기
        sql = "INSERT INTO `test` (SearchId, Sx, Sy, Ex, Ey, STotalTime, STotalDistance, BTotalTime, BTotalDistance, Optipath, Diff) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, tuple(values))
        db.commit()

    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))

    return "ok"

# /saveMongo : 요청해서 mongo에 넣을 data 받기
@app.post("/getMongo/")
async def get_mongo(data:dict): #{"BId": "0007"}
    try:
        response = requests.get("http://192.168.1.64:3000/getMongo")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    data = response.json()  # 전달 받은 데이터를 JSON 형태로 변환
    print(data)
    pathlist = data.get("path_list", [])
    print(pathlist)

    for data_item in pathlist:
        idtype = data_item.get('SearchId')
        if idtype == 'BId':
            mycolbus.insert_one(data_item)
        elif idtype == 'SId':
            mycolsub.insert_one(data_item)

    result = mycolbus.find_one({"BId": "0007"}, {"_id":0})
    return result

# 사용자에게 값 받아서 연산 후 유사 경로 리스트업
def calculate_distance(x1, y1, x2, y2):
    
    return math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)

@app.get("/favpath/")
async def pop_favpath(sx: str, sy: str, ex: str, ey: str):
    try:
        db.connect()  # 데이터베이스 연결
        cursor = db.get_cursor()  # 커서 가져오기
        sql = "SELECT * FROM `sidx`"
        cursor.execute(sql)
        rows = cursor.fetchall()

    except Exception as e:
        raise HTTPException(status_code=500)

    # print(rows)

    matched_paths = []
    # sx, sy, ex, ey = map(float, [sx, sy, ex, ey])

    for row in rows:
        start_distance = calculate_distance(sx, sy, row['Sx'], row['Sy'])
        end_distance = calculate_distance(ex, ey, row['Ex'], row['Ey'])
        
        if start_distance <= 0.0045 and end_distance <= 0.0045:
            matched_paths.append(row)

    print(matched_paths)
    return matched_paths

# @app.get("/getEndBike")
# async def getEndBike():
#     print(data)