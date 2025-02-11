from fastapi import FastAPI
from formdata import formhandling

app = FastAPI()

@app.get("/")
async def health() :
    return {"message" : "App is running fine"}

app.include_router(formhandling.router)