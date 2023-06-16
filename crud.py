from sqlalchemy.orm import Session
import datetime
import models 
import schema

def get_simulation_from_db(db: Session, simulationDate: datetime.date):
    return db.query(models.DataDay).filter(models.DataDay.simulationDate == simulationDate).all()

def get_sample_from_db(db: Session, simulationDate: datetime.date, sample: float):
    return db.query(models.DataDay).filter((models.DataDay.simulationDate == simulationDate)&(models.DataDay.sample == sample)).all()

def get_user(db: Session, username: str):
    user_dict = db.query(models.Users).filter((models.Users.username == username)).first()
    return schema.UserPassword(
        id=user_dict.id,
        username=user_dict.username,
        password_hashed=user_dict.password_hashed,
        disabled=user_dict.disabled
    )

def change_user_password(db: Session, username:str, new_password_hashed:str):
    user = db.query(models.Users).filter((models.Users.username == username)).first()
    user.password_hashed = new_password_hashed
    db.commit()
    db.refresh(user)
    return True

