# from pymongo import MongoClient
# import os
# import json

# # 기본 디렉토리 설정
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# secret_file = os.path.join(BASE_DIR, 'secret.json')  # secret.json 파일의 위치

# # secret.json 파일에서 데이터베이스 설정 정보를 로드
# with open(secret_file) as f:
#     secrets = json.loads(f.read())

# def get_secret(setting, secrets=secrets):
#     """환경 변수를 가져오는 함수"""
#     try:
#         return secrets[setting]
#     except KeyError:
#         errorMsg = f"Set the {setting} environment variable."
#         raise KeyError(errorMsg) from None

# HOSTNAME = get_secret("Mongo_Hostname")
# USERNAME = get_secret("Mongo_Username")
# PASSWORD = get_secret("Mongo_Password")

# #몽고 서버 연결
# uri = f'mongodb://{USERNAME}:{PASSWORD}@{HOSTNAME}'
# client = MongoClient(uri)

# class MonConn:
#     def __init__(self):
#         self.client = MongoClient(uri)
#         self.db = self.client['bikeproject']

#     # 데이터베이스 연결
#     def connect(self, uri, bikeproject):
#         if not self.client:
#             self.client = MongoClient(uri)
#             self.db = self.client[bikeproject]

#     # 데이터베이스 선택
#     def get_database(self, bikeproject=None):
#         if self.client:
#             if bikeproject:
#                 return self.client[bikeproject]
#             return self.db
#         else:
#             raise Exception("Database connection not established.")

#     # 컬렉션 가져오기
#     def get_buspath(self, buspath):
#         if self.db:
#             return self.db[buspath]
#         else:
#             raise Exception("Database not selected.")

#     def get_subwaypath(self, subwaypath):
#         if self.db:
#             return self.db[subwaypath]
#         else:
#             raise Exception("Database not selected.")

#     # 연결 닫기
#     def close_mon(self):
#         if self.client:
#             self.client.close()
#             self.client = None