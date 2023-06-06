from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import datetime


import crud
import models
import schema
from apidb import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()
                    
# @app.get("/ok/")
# def test(db:Session = Depends(get_db)):
#     return crud.selectAllDay(db, simudate=date)

# @app.get("/{simudate}/", response_model=dict[schema.DataDay])
# def read_by_day(simudate: datetime.date, db:Session = Depends(get_db)):
#     data = crud.get_data_by_day(db, simudate=simudate)
#     return data

@app.get("/{simudate}", response_model=list[schema.DataDayWithAllDays])
def read_by_day(simudate: str, db: Session = Depends(get_db)):
    date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
    data = crud.get_data_by_day(db=db, simudate=date_obj)
    return data 

@app.get("/{simudate}/{sample}", response_model=list[schema.DataDayWithAllDays])
def read_by_sample(simudate: str, sample:float, db:Session = Depends(get_db)):
    date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
    data = crud.get_data_by_sample(db=db, simudate=date_obj, sample=sample)
    return data

# @app.get("/{simudate}/pred/{predictionDay}", response_model=list[schema.DataDayWithASingleDay])
# def read_by_prediction_day(simudate: str, predictionDay : int,  db:Session = Depends(get_db)):
#     date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
#     data = crud.get_data_by_prediction_day(db, simudate=date_obj, predictionDay=predictionDay)
#     return data



@app.get("/{simudate}/pred/{prediction_day}")
def read_by_prediction_day(simudate: str, prediction_day: int, Session = Depends(get_db)):
    # Récupérer les données correspondantes au jour de prédiction spécifié
    date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
    data = crud.get_data_by_prediction_day(db=Session, simudate=date_obj, predictionDay=prediction_day)
    return data

