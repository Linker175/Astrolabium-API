from sqlalchemy import create_engine, Column, Integer, Float, Date, JSON, String, Boolean
import numpy as np
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the MariaDB engine using MariaDB Connector/Python
engine = create_engine("mariadb+mariadbconnector://root:lol@127.0.0.1:3306/astrolabium")

Base = declarative_base()

class DataDay(Base):
    __tablename__ = 'testwithdict'
    id = Column(Integer, primary_key=True)
    simulationDate = Column(Date)
    sample = Column(Float)
    targetDays = Column(JSON)
   
class Users(Base):
    __tablename__ = 'users2'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(4),  unique=True, index=True)
    password_hashed = Column(String(60))
    disabled = Column(Boolean, default=True)

Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

#Dependency
def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()                  
