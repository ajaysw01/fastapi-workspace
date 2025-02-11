from fastapi import FastAPI
from .routers import product

app = FastAPI()



@app.get("/")
async def health() : 
    return {"message " : "App is working"}

app.include_router(product.product_router)