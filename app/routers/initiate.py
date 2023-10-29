from fastapi import APIRouter
import uuid

router = APIRouter(
    prefix="/initiate",
    tags=["initiate"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def initiate():
    return {"id": str(uuid.uuid4())}
