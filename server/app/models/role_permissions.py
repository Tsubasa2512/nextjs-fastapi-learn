from sqlalchemy import Column, Integer, ForeignKey
from ..database import Base

class RolePermissions(Base):
    __tablename__="role_permissions"

    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'), primary_key=True)