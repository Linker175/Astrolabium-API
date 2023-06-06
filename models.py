from sqlalchemy import Column, Integer, Float, Date
from apidb import Base

class DataDay(Base):
    __tablename__ = 'dataday'
    id = Column(Integer, primary_key=True)
    simudate = Column(Date)
    sample = Column(Integer)
    for i in range(1, 181):
       locals()[f'day{i}'] = Column(Float)
