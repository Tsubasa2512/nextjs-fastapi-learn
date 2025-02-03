from pydantic import BaseModel

class Permissions(BaseModel):
    id:int
    name:str
    resource:str

    class Config:
        orm_mode = True