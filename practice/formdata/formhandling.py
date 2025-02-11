from fastapi import Form, APIRouter
from typing_extensions import Annotated

router = APIRouter()

@router.post("/login/")
async def login(username : Annotated[str,Form()],password : Annotated[str, Form()]) :
    return {"user" : username}