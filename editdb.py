from datetime import date
import numpy as np
from db import Session   
from db import DataDay

session = Session()

day_values = {}
for i in range(1, 181):
    day_values[f'day{i}'] = float(np.random.random()*1000)

def addSimulationDay(date, nbsample):
    for sample in range(1, nbsample+1):
        new_row = DataDay()
        new_row.simudate = date
        new_row.sample = sample
        for key, value in day_values.items():
            setattr(new_row, key, value)
        session.add(new_row)
        session.commit()

def selectAllDay():
    dataday = session.query(DataDay).all()
    for data in dataday:
        print(" - " + str(data.simudate) + ' ' + str(data.sample) + ' ', end='')
        for day in range(1, 181):
            dynamic_attr = data.day_columns[str(day)]
            print(dynamic_attr, end=' ')
        print("\n")


def DeleteDB():
    session.query(DataDay).delete()
    session.commit()


# Add some new simulations
addSimulationDay(date(2023, 5, 29), 3)

# Show all simulations
print('Simulation Day')
#selectAllDay()

#DeleteDB()