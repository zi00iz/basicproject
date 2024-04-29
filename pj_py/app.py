import math
import uvicorn
import requests, json
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import pymysql
# from pydantic import BaseModel
from database import db_conn
from models import Sidx
from typing import Union, Optional, List

app = FastAPI()

db = db_conn()
session = db.sessionmaker()

# json_url = 'jiyoung json 서버/'

# #savesql
# @app.get("/saveSql")
# async def save_sql():
#     response = requests.get("API주소")

#     if response.status_code != 200:
#         raise HTTPException(status_code=400, detail="정보를 가져오는 것에 실패했습니다.")

#     #응답 데이터를 JSON 형태로 변환
#     data = response.json()

# @app.get("/getMongo")
# async def get_mongo():
#     response = requests.get("지원주소")
    
#     if response.status_code != 200:
#         raise HTTPException(status_code=400, detail="정보를 가져오는 것에 실패했습니다.")
    
    

# 파라미터로 받은 사용자의 데이터와 비교하기
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)

@app.get("/favpath/")
async def pop_path(sx: str, sy: str, ex: str, ey: str):
    print(sx, sy, ex, ey )
    connection = db.connection()  # 데이터베이스 연결 생성
    try:
        cursor = connection.cursor()  # 커서 생성
        cursor.execute("SELECT * FROM sidx")
        rows = cursor.fetchall()

        matched_paths = []

        for row in rows:
            start_distance = calculate_distance(sx, sy, row[1], row[2])
            end_distance = calculate_distance(ex, ey, row[3], row[4])

            #거리 계산하기
            if start_distance <= 0.0045 and end_distance <= 0.0045:
                matched_paths.append({
                    'Sid': row[0],
                    'Sx': row[1],
                    'Sy': row[2],
                    'Ex': row[3],
                    'Ey': row[4],
                    'Type': row[5]
                })

        return matched_paths
        
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        connection.close()

# @app.get('/endbike/', response_model=List[StationInfo])
# async def endbike(ex: float, ey: float):
#     # JSON 서버에서 데이터 가져오기
#     response = requests.get(json_url)
#     if response.status_code != 200:
#         raise HTTPException(status_code=404, detail="JSON 데이터를 불러오는데 실패했습니다.")
#     data = response.json()

#     nearby_stations = []

#     #연산 및 조건식
#     for item in data:
#         # 사용자의 좌표와 각 스테이션의 좌표 간의 거리 계산
#         distance = calculate_distance(ex, ey, item['x'], item['y'])
#         # 거리가 500 이하인 경우 리스트에 추가
#         if distance <= 0.0045:
#             nearby_stations.append(StationInfo(**item))

#     return nearby_stations

# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=5000)

# @app.get('/')