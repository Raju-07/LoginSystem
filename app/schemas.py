import uuid
from pydantic import BaseModel,Field,EmailStr,ConfigDict
from typing import Optional
from datetime import datetime

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class UserRegisterRequest(Base):
    name : str = Field(min_length=3,default='')
    username : str = Field(min_length=3,default='')
    email: EmailStr = Field(default="user@gmail.com")
    password: str = Field(min_length=6,default='')

class UserRegisterResponse(Base):
    id : uuid.UUID
    name : str
    username : str
    email : str

# GET USER SCHEMA
class UserDataResponse(Base):
    id: uuid.UUID
    name: str
    email : str
    role : str 
    is_active : bool
    created_at : datetime
