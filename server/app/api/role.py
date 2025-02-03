from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud,database
from app.schemas.role  import Role as RoleSchema
from app.schemas.role import CreateRole

router = APIRouter()

@router.get('/role', response_model=list[RoleSchema])
def read_role(skip:int = 0, limit: int = 100,db:Session = Depends(database.get_db)):
    role = crud.get_role(db=db, skip=skip, limit=limit)
    return role

@router.get('/role/{id}', response_model=RoleSchema)
def show_role(id:int, skip:int= 0, limit:int =100, db:Session = Depends(database.get_db)):
    role = crud.show_role(db=db, id=id, skip=skip,limit=limit)
    return role

@router.post('/role')
def create_role(role_add:CreateRole,db:Session = Depends(database.get_db)):
    role = crud.create_role(db,role_add)
    return role

@router.put('/role/{id}', response_model=RoleSchema)
def update_role(id: int, role_data: CreateRole, db: Session = Depends(database.get_db)):
    updated_role = crud.update_role(db=db, id=id, role_data=role_data)
    if updated_role:
        return updated_role
    else:
        raise HTTPException(status_code=404, detail="Role not found")


@router.delete('/role/{id}')
def delete_role(id:int, db:Session = Depends(database.get_db)):
    crud.delete_role(db,id=id)
    return {"message":"Delete Success"}