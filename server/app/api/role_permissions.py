from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud,schemas,database
from app.schemas.role_permissions import RolePermissions

router = APIRouter()

@router.get("/role-permissions",response_model=list[RolePermissions])
def read_role_permissions(skip:int = 0 , limit:int = 100, db:Session = Depends(database.get_db)):
    role_permissions = crud.get_role_permission(db=db, skip=skip, limit=limit)
    return role_permissions