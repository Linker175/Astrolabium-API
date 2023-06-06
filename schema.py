from pydantic import BaseModel, create_model
from datetime import date  
from typing import Dict

class DataDayBase(BaseModel):
    simudate: date
    sample : int

class DataDay(DataDayBase):
    class Config:
        orm_mode = True 

additional_days_fields = {f"day{i}": (float, None) for i in range(1, 181)}

DataDayWithAllDays = create_model(
    "DataDayWithAllDays",
    __base__=DataDay,
    **additional_days_fields,
)

field = {
    "day1" : (float,None)
} 

DataWithDay1 = create_model(
    "DataWithDay1",
    __base__=DataDay,
   **field,
)




