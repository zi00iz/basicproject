# from fastapi import FastAPI, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.future import select
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, JSON
# import asyncio

# DATABASE_URL = "mysql+aiomysql://your_username:your_password@localhost/your_db_name"
# engine = create_async_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
# Base = declarative_base()

# # 모델 정의
# class Data(Base):
#     __tablename__ = "data"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(JSON)

# app = FastAPI()

# # 데이터베이스 초기화 함수
# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# # 비동기 ORM 사용을 위한 세션 생성
# async def get_db_session():
#     async_session = SessionLocal()
#     try:
#         yield async_session
#     finally:
#         await async_session.close()

# @app.on_event("startup")
# async def startup_event():
#     await init_db()

# @app.get("/getSql")
# async def get_sql(data: str, db: AsyncSession = Depends(get_db_session)):
#     new_data = Data(content=data)
#     db.add(new_data)
#     await db.commit()
#     return {"message": "Data successfully saved to MySQL", "data": data}

# #----
# from fastapi import FastAPI, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.future import select
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, JSON
# import asyncio

# DATABASE_URL = "mysql+aiomysql://your_username:your_password@localhost/your_db_name"
# engine = create_async_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
# Base = declarative_base()

# # 모델 정의
# class Data(Base):
#     __tablename__ = "data"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(JSON)

#app = FastAPI()

# 데이터베이스 초기화 함수
# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# 비동기 ORM 사용을 위한 세션 생성
# async def get_db_session():
#     async_session = SessionLocal()
#     try:
#         yield async_session
#     finally:
#         await async_session.close()

# @app.on_event("startup")
# async def startup_event():
#     await init_db()

# @app.get("/getSql")
# async def get_sql(data: str, db: AsyncSession = Depends(get_db_session)):
#     new_data = Data(content=data)
#     db.add(new_data)
#     await db.commit()
#     return {"message": "Data successfully saved to MySQL", "data": data}

#--
#다른 Api가 보내준 sql 받기
# @app.get("/getSql")
# async def get_sql(data: str, db: AsyncSession = Depends(get_db_session)):
#     new_data = Data(content=data)
#     db.add(new_data)
#     await db.commit()
#     return {"message": "Data successfully saved to MySQL", "data": data}

# # 데이터베이스에 저장하기
# try:
#     db_instance = db_conn()                 # 데이터베이스 연결 인스턴스 생성
#     session = db_instance.sessionmaker()    # SQLAlchemy 세션 생성
    
#     save_sql_data = sidx(
#         SId=data['sql']['sid'],
#         Sx=data['sql']['Sx'],
#         Sy=data['sql']['Sy'],
#         Ex=data['sql']['Ex'],
#         Ey=data['sql']['Ey'],
#         Type=data['sql']['Type']
#     )

#     session.add(save_sql_data)  # 세션에 새 데이터 추가
#     session.commit()  # 변경사항 데이터베이스에 반영
    
# except Exception as e:
#     session.rollback()  # 오류 발생 시 롤백
#     raise HTTPException(status_code=500, detail="데이터베이스에 데이터를 저장하는 데 실패했습니다.") from e

# finally:
#     session.close()  # 세션 닫기

# return {"status": "OK", "data": {"sIdx": data['sql']['sIdx']}}