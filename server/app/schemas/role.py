# schemas/role.py

from pydantic import BaseModel
from typing import List
from .permissions import Permissions

class RoleBase(BaseModel):
    name: str

class CreateRole(RoleBase):
    permissions: List[int]  # Chỉ nhận vào một danh sách các ID

class Role(RoleBase):
    id: int
    permissions: List[Permissions]  # Sử dụng schema Permissions để trả về dữ liệu

    class Config:
        orm_mode = True
