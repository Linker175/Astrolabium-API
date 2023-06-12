from sqlalchemy import Column, Integer, Date, JSON
from db import Base

class DataDay(Base):
    __tablename__ = 'testwithdict'
    id = Column(Integer, primary_key=True)
    simudate = Column(Date)
    sample = Column(Integer)
    days = Column(JSON)