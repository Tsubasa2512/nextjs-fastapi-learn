from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud,schemas,database
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()

@router.get("/users", response_model=list[User])
def read_user(skip:int = 0, limit:int =100, db:Session = Depends(database.get_db)):
    users = crud.get_users(db=db, skip=skip,limit=limit)
    return users

@router.get("/user/{id}", response_model=User)
def read_user(id:int, db:Session = Depends(database.get_db)):
    user = crud.show_user(db=db, id=id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not foun")
    return user

@router.put("/user/{id}", response_model= User )
def update_user(id:int, user_update:UserUpdate, db:Session = Depends(database.get_db)):
    user = crud.update_user(db=db, id=id, user_update=user_update)
    return user

@router.delete("/user/{id}")
def delete_user(id:int, db:Session = Depends(database.get_db)):
    crud.delete_user(db,id=id)
    return{"message":"Delete Success"}

@router.post("/user",response_model=User)
def create_user(user_add:UserCreate, db:Session = Depends(database.get_db)):
    user = crud.create_user(db, user_add)
    return user
