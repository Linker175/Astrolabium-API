from datetime import date
import numpy as np
from db import Session   
from db import DataDay, Users
import json

session = Session()

def add_simulation(date, numberOfSample):
    for sample in range(1, numberOfSample+1):
        targetDaysData = {str(i) : float(np.random.random()*1000) for i in range(1,181)}
        new_row = DataDay()
        new_row.simulationDate = date
        new_row.sample = sample
        new_row.targetDays = json.loads(json.dumps((targetDaysData)))
        session.add(new_row)
        session.commit()

def select_simulation():
    dataday = session.query(DataDay).all()
    for data in dataday:
        print(data.targetDays)
        print("\n")
    print(data.targetDays['1'])

def add_user(username, password_hashed, disabled=True):
    new_user = Users()
    new_user.username = username
    new_user.password_hashed = password_hashed
    new_user.disabled = disabled
    session.add(new_user)
    session.commit()

def select_user():
    users = session.query(Users).all()
    for user in users:
        print(user.username, end='\n')
        print(user.password_hashed, end='\n')
        print(str(user.disabled), end='\n')
        print('\n')

def delete_simulation():
    session.query(DataDay).delete()
    session.commit()

def delete_users():
    session.query(Users).delete()
    session.commit()

# Add some new simulations
#add_user('yoan','$2b$12$d4ksZ0rx5pkLAo4gdI1aDuc.t3XTCpx2c5D0.fWDanwapiH8soV0O',False)
#select_user()

