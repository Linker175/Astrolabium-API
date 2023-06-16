from fastapi import Depends, FastAPI, Body, Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from db import engine
from db import get_db
import crud
import models
import schema
import authentification
import getsimulation

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Endpoints for data
@app.post("/getSimulation", response_model=list[schema.DataDay])
def getSimulation(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload: schema.DataDayBase,
    db: Session = Depends(get_db)
):
    return getsimulation.get_simulation(simulationDate=payload.simulationDate, db=db)

@app.post("/getSimulationSample", response_model=schema.DataDay)
def getSimulationSample(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    payload : schema.DataDaySample,
    db:Session = Depends(get_db)
):
    return getsimulation.get_simulation_sample(simulationDate=payload.simulationDate,sample=payload.sample,db=db)

@app.post("/getSimulationForTargetDay", response_model=list[schema.DataDayForTargetedDay])
async def getSimulation(
    current_user: Annotated[schema.User,Depends(authentification.get_current_active_user)],
    payload: schema.DataDayTargetedDay,
    db:Session = Depends(get_db)
):
    return getsimulation.get_simulation_for_target_day(simulationDate=payload.simulationDate,targetedDay=payload.targetedDay,db=db)


#Endpoints for authentification
@app.post("/login", response_model=schema.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db:Session = Depends(get_db)
):
    return authentification.login_the_user_for_access_token(form_data=form_data,db=db)

@app.get("/user/me/", response_model=schema.User)
async def read_user_me(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)]
):
    return current_user

@app.post("/user/password/")
async def read_user_password(
    current_user: Annotated[schema.User, Depends(authentification.get_current_active_user)],
    password_form: schema.PasswordChangeForm = Depends(),
    db:Session=Depends(get_db)
):
    return authentification.manage_password_changement(current_user=current_user,password_form=password_form,db=db)

