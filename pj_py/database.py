import pymysql
import os.path
import json

# from models import Base

# 기본 디렉토리 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
secret_file = os.path.join(BASE_DIR, 'secret.json')  # secret.json 파일의 위치

# secret.json 파일에서 데이터베이스 설정 정보를 로드
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """환경 변수를 가져오는 함수"""
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {setting} environment variable."
        return KeyError(errorMsg)

# MYSQL 데이터베이스 연결 정보 설정
HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_Port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")

# 데이터베이스 URL 구성
# DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

class dbConn:
    def __init__(self):
        self.connection = None

    # 데이터베이스 연결
    def connect(self):
        if not self.connection:
            self.connection = pymysql.connect(host=HOSTNAME,
                                                user=USERNAME,
                                                password=PASSWORD,
                                                db=DBNAME,
                                                port=int(PORT),
                                                charset='utf8',
                                                cursorclass=pymysql.cursors.DictCursor)
        return self.connection

    # 커서 가져오기
    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise Exception("Database connection not established.")
    
    # 연결 닫기
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    # 롤백 수행
    def rollback(self):
        if self.connection:
            self.connection.rollback()

    #커밋 수행
    def commit(self):
        if self.connection:
            self.connection.commit()