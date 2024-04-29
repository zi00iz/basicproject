from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
import json
from models import Base

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
        errorMsg = "Set the {} environment variable.".format(setting)
        return KeyError(errorMsg)

# 데이터베이스 연결 정보 설정
HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_Port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")

# 데이터베이스 URL 구성
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

class db_conn:
    #세션 생성자 초기화
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500, echo=True)  # echo=True는 로그를 활성화합니다.

    #데이터베이스 세션 생성
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    #데이터베이스 직접 연결
    def connection(self):
        conn = self.engine.connect()
        return conn
    
    #세션 닫기
    def close(self):
        self.connection.close()

    # 세션에 대한 롤백 수행
    def rollback(self):
        self.session.rollback()