from fastapi import APIRouter,Depends
from ..repos import productrepo
from sqlalchemy.orm import Session
from ..db import database 
from typing import List
from ... import schemas
product_router = APIRouter(
    tags=["/product,"],
    prefix="/product"
)

get_db =  database.get_db

product_router.get("/",response_model=List[schemas.Product])
async def get_all_products(db:Session=Depends(get_db)) : 
    return productrepo.getAll()

product_router.post("/")
async def add_product() : 
    pass

product_router.get("/")
async def get_product_by_id() : 
    pass

product_router.put("/")
async def update_product() : 
    pass

product_router.delete("/")
async def delete_product() : 
    pass