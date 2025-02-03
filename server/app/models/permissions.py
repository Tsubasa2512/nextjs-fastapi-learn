from ..database import Base
from sqlalchemy import Column,Integer,String

class Permissions(Base):
    __tablename__ ="permissions"

    id =Column(Integer, primary_key=True, index=True)
    name =Column(String)
    resource = Column(String)