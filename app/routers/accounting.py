from typing import Dict, List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.accounting.factory import ProviderFactory
from app.routers.sheet import SheetItem

router = APIRouter(
    prefix="/accounting",
    tags=["accounting"],
    responses={404: {"description": "Not found"}},
)


class BusinessDetails(BaseModel):
    name: str
    year: int
    provider: str


@router.post("/fetch_balance_sheet/{id}", response_model=List[SheetItem])
async def fetch_balance_sheet(id: str, details: BusinessDetails):
    factory = ProviderFactory()
    provider = factory.get_provider(details.provider)
    return provider.get_balance_sheet(details)
