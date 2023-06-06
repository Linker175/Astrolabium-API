from sqlalchemy.orm import Session
import datetime
import models

def get_data_by_day(db: Session, simudate: datetime.date):
    return db.query(models.DataDay).filter(models.DataDay.simudate == simudate).all()

def get_data_by_sample(db: Session, simudate: datetime.date, sample: float):
    return db.query(models.DataDay).filter((models.DataDay.simudate == simudate)&(models.DataDay.sample == sample)).all()

def get_data_by_prediction_day(db: Session, simudate: datetime.date, predictionDay: int):
    day_column = getattr(models.DataDay, f"day{predictionDay}")
    query =  db.query(day_column).filter(models.DataDay.simudate == simudate).all()
    return [(row[0],) for row in query]
