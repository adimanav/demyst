from typing import Dict
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.accounting.factory import ProviderFactory

router = APIRouter(
    prefix="/accounting",
    tags=["accounting"],
    responses={404: {"description": "Not found"}},
)


class BusinessDetails(BaseModel):
    name: str
    year: int
    provider: str


@router.post("/fetch_balance_sheet/{id}")
async def fetch_balance_sheet(id: str, details: BusinessDetails):
    factory = ProviderFactory()
    provider = factory.get_provider(details.provider)
    return provider.get_balance_sheet(details)
