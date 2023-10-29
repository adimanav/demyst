from typing import Dict
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.decision.engine import DecisionDetails
from app.decision.engine import DecisionEngine 

router = APIRouter(
    prefix="/decision",
    tags=["decision"],
    responses={404: {"description": "Not found"}},
)


class Details(BaseModel):
    name: str
    year: int
    profit_or_loss: dict[int, float]
    preassessment: float


@router.get("/")
async def decide(details: Details):
    decision_engine = DecisionEngine()

    decision_details = DecisionDetails()
    decision_details.name = details.name
    decision_details.year = details.year
    decision_details.profit_or_loss = details.profit_or_loss
    decision_details.preassessment = details.preassessment

    return decision_engine.request(decision_details)
