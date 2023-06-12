from pydantic import BaseModel, Json
from typing import Any, List
from datetime import date  
import json

class DataDayBase(BaseModel):
    simudate: date

class DataDay(DataDayBase):
    sample : int
    days : dict[str,float]
    class Config:
        orm_mode = True 







