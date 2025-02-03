from sqlalchemy.orm import Session
from app.models.product import Product
from app import schemas

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def show_product(db:Session, id:int):
    return db.query(Product).filter(Product.id == id).first()

def update_product(db:Session, id:int, product_update: schemas.ProductUpdate):
    product = db.query(Product).filter(Product.id == id).first()
    if product:
        if product_update.name:
            product.name = product_update.name
        if product_update.description:
            product.description = product_update.description
        if product_update.price:
            product.price = product_update.price
        if product_update.category_id:
            product.category_id = product_update.category_id    
        db.commit()
        db.refresh(product)
        return product
    return None   

def delete_product(db:Session, id:int):
    product =  db.query(Product).filter(Product.id == id).first()
    if product:
        db.delete(product)
        db.commit()

def create_product(db:Session, product_add: schemas.ProductCreate):
    product = Product(name=product_add.name, description=product_add.description, price=product_add.price, category_id= product_add.category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# def create_product(db: Session, product: schemas.ProductCreate):
#     db_product = Product(name=product.name, description=product.description, price=product.price)
#     db.add(db_product)
#     db.commit()
#     db.refresh(db_product)
#     return db_product
