import sqlalchemy
from datetime import date   
import numpy as np
from sqlalchemy.orm import declarative_base

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://admin_user:lol@127.0.0.1:3306/results")

Base = declarative_base()

class DataDay(Base):
    __tablename__ = 'dataday'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    simudate = sqlalchemy.Column(sqlalchemy.Date)
    sample = sqlalchemy.Column(sqlalchemy.Double)
    days = {}

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def addSimulationDay(date, nbsample):
    for sample in range(1, nbsample+1):
        new_row = DataDay()
        new_row.simudate = date
        new_row.sample = sample
        for day in range(1, 25):
            new_row.days[str(day)] = np.random.random() * 10000
        session.add(new_row)
        session.commit()

def selectAllDay():
    dataday = session.query(DataDay).all()
    for data in dataday:
        print(" - " + str(data.simudate) + ' ' + str(data.sample) + ' ', end='')
        for day in range(1, 25):
            dynamic_attr = data.days.get(str(day))
            print(dynamic_attr, end=' ')
        print("\n")

def DeleteDB():
    session.query(DataDay).delete()
    session.commit()

# Add some new simulations
addSimulationDay(date(2023, 5, 29), 1)

# Show all simulations
print('Simulation Day')
selectAllDay()

DeleteDB()