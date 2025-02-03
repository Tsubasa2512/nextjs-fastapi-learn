from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str]  # xử lý null 
    price: float
    category_id:int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name:Optional[str] = None
    description:Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None

class Product(ProductBase):
    id: int 

    class Config:
        orm_mode = True
