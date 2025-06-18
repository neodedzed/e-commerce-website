from fastapi import APIRouter, Depends

from crud.product_crud import read_all_products
from database.db import get_db
from sqlalchemy.orm import Session

from routes.schemas.product_schema import Products

product_router = APIRouter()

@product_router.get('/', response_model=[Products])
def get_all_products(db: Session=Depends(get_db)):
    products = read_all_products(db)
    return products