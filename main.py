from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import datetime
import json

import crud
import models
import schema
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()
                    
@app.get("/{simudate}", response_model=list[schema.DataDay])
def read_by_day(simudate: str, db: Session = Depends(get_db)):
    date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
    data = crud.get_data_by_day(db=db, simudate=date_obj)
    return data

@app.get("/{simudate}/{sample}", response_model=schema.DataDay)
def read_by_sample(simudate: str, sample:float, db:Session = Depends(get_db)):
    date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
    data = crud.get_data_by_sample(db=db, simudate=date_obj, sample=sample)
    return data[0]

@app.get("/{simudate}/pred/{prediction_day}", response_model=list[schema.DataDay])
def read_by_prediction_day(simudate: str, prediction_day: str, db:Session = Depends(get_db)):
    date_obj = datetime.datetime.strptime(simudate, "%Y-%m-%d").date()
    data = crud.get_data_by_day(db=db, simudate=date_obj)
    output = []
    for k in range(len(data)):
        simudateJson = data[k].simudate
        sampleJson = data[k].sample
        daysJson = data[k].days[prediction_day]
        output.append({
            'simudate':simudateJson,
             'sample':sampleJson,
             'days':{
                 str(prediction_day):daysJson
                }
        })
    return output

