from fastapi import APIRouter

router = APIRouter(
    tags=["Health Check"]
)

@router.get("/")
def healthCheck():
    return {"message : ":"App is working...."}