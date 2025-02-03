from sqlalchemy.orm import Session
from app.models.role_permissions import RolePermissions

def get_role_permission(db:Session , skip:int = 0, limit: int= 100):
    return db.query(RolePermissions).offset(skip).limit(limit).all()