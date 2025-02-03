from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship
from ..database import Base

class Role(Base):
    __tablename__ ="roles"

    id = Column(Integer , primary_key=True, index=True)
    name = Column(String, index=True)
    permissions = relationship("Permissions", secondary="role_permissions", backref="roles")

