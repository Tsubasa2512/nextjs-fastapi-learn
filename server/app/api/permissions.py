from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas,database
from app.schemas.permissions import Permissions

router = APIRouter()
@router.get("/permissions",response_model=list[Permissions])
def read_permissions(skip:int = 0, limit:int =100, db:Session = Depends(database.get_db)):
    permisions = crud.get_permissions(db= db, skip=skip, limit=limit)
    return permisions
