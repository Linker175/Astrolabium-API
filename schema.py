from pydantic import BaseModel, Json, Field
from fastapi import Form
from typing import Annotated
from datetime import date 

#range of queries
sampleMin=1
sampleMax=3 

targetDayMin=1
targetDayMax=180

#Simulation Class
class DataDayBase(BaseModel):
    simulationDate: date

class DataDaySample(DataDayBase):
    sample : int = Field(..., ge=sampleMin, le=sampleMax, description="From 1 to 100000", example=1)

class DataDayTargetedDay(DataDayBase):
    targetedDay : int = Field(..., ge=targetDayMin, le=targetDayMax, description="From 1 to 180", example=8)

class DataDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={'1':0,'2':0,'3':0})
    class Config:
        orm_mode = True
        
class DataDayForTargetedDay(DataDayBase):
    sample : int = Field(..., example=1)
    targetDays : dict[str,float] = Field(..., example={'8':0})
    class Config:
        orm_mode = True          

#Authentifiation Class
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    disabled: bool | None = None

class UserPassword(User):
    password_hashed: str

class PasswordChangeForm(BaseModel):
    old_password_plain: Annotated[str, Form(..., description="Your old password")]
    new_password_plain: Annotated[str, Form(..., description="Your new password")]
    new_password_confirmation_plain: Annotated[str, Form(..., description="Confirm your new password")]






