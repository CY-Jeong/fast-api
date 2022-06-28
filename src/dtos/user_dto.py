from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class UserDto(BaseModel):
    name: Optional[str] = Field(default="cyj", alias = "Name")
    age: Optional[int] = 20

class Gender(Enum):
    male = "male"
    female = "female"
    trans = "trans"
    others = "-1"
