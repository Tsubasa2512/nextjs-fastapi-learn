# app/api/product.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database
from app.schemas.category import Category  # Thử import trực tiếp từ product.py

router = APIRouter()

@router.get("/category", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_categories(db=db, skip=skip, limit=limit)
    return products
