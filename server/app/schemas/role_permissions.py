from pydantic import BaseModel


class RolePermissions(BaseModel):
    role_id:int
    permission_id:int

    class Config:
        orm_mode = True  