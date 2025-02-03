from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas,database
from app.schemas.user import LoginRequest

router = APIRouter()

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(database.get_db)): 
    check = crud.authenticate_user(db,request.username, request.password)
    if check:
        return {"message": "Login successful", "token": check}  # Trả về token
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")