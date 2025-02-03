from pydantic import BaseModel
from typing import Optional
from datetime import datetime  
from .role import Role

class LoginRequest(BaseModel):
    username:str
    password:str


class UserBase(BaseModel):
    username:str
    password_hash:str
    email:str

class UserCreate(UserBase):
    role_id:int    

class UserUpdate(UserBase):
    username:Optional[str]
    email:Optional[str]
    password_hash:Optional[str] = None
    role_id:int

class User(UserBase):
    id:int
    updated_at:datetime
    role: Optional[Role] 
    
    class Config:
        orm_mode = True
