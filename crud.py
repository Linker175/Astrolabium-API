from sqlalchemy.orm import Session
from sqlalchemy import func
import datetime
import models 

def get_data_by_day(db: Session, simudate: datetime.date):
    return db.query(models.DataDay).filter(models.DataDay.simudate == simudate).all()

def get_data_by_sample(db: Session, simudate: datetime.date, sample: float):
    return db.query(models.DataDay).filter((models.DataDay.simudate == simudate)&(models.DataDay.sample == sample)).all()


# use the jsonlib daysfield and get "1"
# rejex : search for the string that start with the " " with the quote
    
