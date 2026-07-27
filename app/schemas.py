import uuid
from pydantic import BaseModel,Field,EmailStr,ConfigDict
from typing import Optional

class Base(BaseModel):
    class_config = ConfigDict(from_attributes=True)

class UserRegisterRequest(Base):
    full_name : str
    username : str
    email: EmailStr
    password: str

class UserRegisterResponse(Base):
    id : uuid.UUID
    full_name : str
    username : str
    email : str
