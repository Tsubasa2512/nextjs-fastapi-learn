# app/crud/product.py
from sqlalchemy.orm import Session
from app.models.category import Category  # Import Product đúng từ models.product
from app import schemas

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

# def create_product(db: Session, product: schemas.ProductCreate):
#     db_product = Product(name=product.name, description=product.description, price=product.price)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product

