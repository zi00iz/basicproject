# from sqlalchemy import Column, Integer, VARCHAR
# from sqlalchemy.ext.declarative import declarative_base
# # from pydantic import BaseModel

# Base = declarative_base()

# class Sidx(Base):
#     __tablename__ = 'sidx'

#     sid = Column(Integer, nullable=False, primary_key=True)
#     sx = Column(VARCHAR(45), nullable=False)
#     sy = Column(VARCHAR(45), nullable=False)
#     ex = Column(VARCHAR(45), nullable=False)
#     ey = Column(VARCHAR(45), nullable=False)
#     Type = Column(VARCHAR(45), nullable=False)

# class bikestation(BaseModel):
#     stationNo: int
#     stationName: str
#     addr: str
#     x: float
#     y: float