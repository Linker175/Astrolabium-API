from datetime import date
import numpy as np
from db import Session   
from db import DataDay
import json

session = Session()

def addSimulationDay(date, nbsample):
    for sample in range(1, nbsample+1):
        daysdata = {str(i) : float(np.random.random()*1000) for i in range(1,181)}
        new_row = DataDay()
        new_row.simudate = date
        new_row.sample = sample
        new_row.days = json.loads(json.dumps((daysdata)))
        session.add(new_row)
        session.commit()

def selectAllJSON():
    dataday = session.query(DataDay).all()
    for data in dataday:
        print(data.days)
        print("\n")

    print(data.days['1'])


def DeleteDB():
    session.query(DataDay).delete()
    session.commit()

# Add some new simulations
selectAllJSON()

