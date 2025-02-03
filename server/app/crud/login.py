import bcrypt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas
from app.models.user import User
from app.models.role_permissions import RolePermissions

import jwt
import datetime
import secrets
SECRET_KEY =secrets.token_urlsafe(32)
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict, expires_delta: datetime.timedelta = None ):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() +expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)    
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def hash_password(password:str) ->str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(stored_hash:str, password:str)->bool:
    return bcrypt.checkpw(password.encode('utf-8'),stored_hash.encode('utf-8'))


def authenticate_user(db:Session,username:str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(user.password_hash ,password):
        access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

        role_permissions = db.query(RolePermissions).filter(RolePermissions.role_id == user.role_id).all()
        permissions = [rp.permission_id for rp in role_permissions]

        return {"access_token": access_token, "token_type": "bearer","role_id":permissions}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )
