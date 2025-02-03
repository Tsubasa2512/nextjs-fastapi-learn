from sqlalchemy.orm import Session, joinedload
from app.models.role import Role
from app import schemas
from app.models.permissions import Permissions  
from app.schemas.role import CreateRole
from app.models.role_permissions import RolePermissions

def get_role(db:Session, skip:int = 0, limit: int = 100):
    return db.query(Role).options(joinedload(Role.permissions)).offset(skip).limit(limit).all()

def show_role(db:Session ,id:int, skip:int = 0, limit:int =100):
    return db.query(Role).options(joinedload(Role.permissions)).filter(Role.id == id).first()

def create_role(db:Session,role_add:schemas.Role):
    role=Role(name=role_add.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    if role_add.permissions:
        role_permissions = [
            RolePermissions(role_id=role.id, permission_id=perm_id)
            for perm_id in role_add.permissions
        ]
        db.add_all(role_permissions)
        db.commit()
        return True
    return None

def update_role(db: Session, id: int, role_data: CreateRole):
    db_role = db.query(Role).filter(Role.id == id).first()
    if not db_role:
        return None  
    db_role.name = role_data.name
    permissions = db.query(Permissions).filter(Permissions.id.in_(role_data.permissions)).all()
    db_role.permissions = permissions  
    db.commit()
    db.refresh(db_role)
    return db_role


def delete_role(db:Session,id:int):
    role= db.query(Role).filter(Role.id == id).first()
    if role:
        db.delete(role)
        db.commit()
