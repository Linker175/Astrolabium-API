import sqlalchemy 
import numpy as np
from sqlalchemy.orm import declarative_base
import datetime

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:lol@127.0.0.1:3306/astrolabium")

Base = declarative_base()

class DataDay(Base):
    __tablename__ = 'testwithdict'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    simudate = sqlalchemy.Column(sqlalchemy.Date)
    sample = sqlalchemy.Column(sqlalchemy.Float)
    days = sqlalchemy.Column(sqlalchemy.JSON)
   

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
