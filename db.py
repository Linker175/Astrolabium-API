import sqlalchemy 
import numpy as np
from sqlalchemy.orm import declarative_base
import datetime

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://admin_user:lol@127.0.0.1:3306/results4")

Base = declarative_base()

class DataDay(Base):
    __tablename__ = 'dataday'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    simudate = sqlalchemy.Column(sqlalchemy.Date)
    sample = sqlalchemy.Column(sqlalchemy.Float)
    # Add Float columns from day1 to day180
    for i in range(1, 181):
       locals()[f'day{i}'] = sqlalchemy.Column(sqlalchemy.Float)
    # day_columns = {}
    # for day in range(1, 181):
    #     day_columns[str(day)] = sqlalchemy.Column(sqlalchemy.Float)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


# Add some new simulations
#addSimulationDay(date(2023, 5, 29), 1000)

# Show all simulations
#print('Simulation Day')
#selectAllDay()

#DeleteDB()