from sqlalchemy.orm import Session
from app.models.permissions import Permissions

def get_permissions(db:Session, skip:int = 0, limit: int = 100):
    return db.query(Permissions).offset(skip).limit(limit).all()