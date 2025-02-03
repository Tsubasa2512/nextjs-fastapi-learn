from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
from app.schemas.product import Product, ProductUpdate,ProductCreate

router = APIRouter()

@router.get("/products", response_model=list[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    products = crud.get_products(db=db, skip=skip, limit=limit)
    return products

@router.get("/products/{id}", response_model=Product)
def read_product(id: int, db: Session = Depends(database.get_db)):
    product = crud.show_product(db=db , id=id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{id}", response_model=Product)
def update_product(id: int, product_update: ProductUpdate, db: Session = Depends(database.get_db)):
    product = crud.update_product(db, id=id, product_update=product_update)
    return product

@router.delete("/products/{id}")
def delete_product(id:int, db:Session = Depends(database.get_db)):
    crud.delete_product(db, id=id)
    return {"message": "Delete Success"}

@router.post("/products",response_model=Product)
def create_product( product_add:ProductCreate , db:Session = Depends(database.get_db)):
    product = crud.create_product(db, product_add)
    return product
