from sqlalchemy import Column , Integer, String,DateTime, ForeignKey
from app.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id =Column(Integer, primary_key= True, index=True)
    username = Column(String, unique=True, index=True)
    email =Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role")
    password_hash = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
