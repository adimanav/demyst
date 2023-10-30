from datetime import date
from dateutil.relativedelta import relativedelta
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from app.decision.engine import DecisionDetails
from app.decision.engine import DecisionEngine
from app.routers.sheet import SheetItem

router = APIRouter(
    prefix="/decision",
    tags=["decision"],
    responses={404: {"description": "Not found"}},
)


class Details(BaseModel):
    name: str
    year: int
    sheet: List[SheetItem]
    amount: float


@router.post("/")
async def decide(details: Details):
    decision_engine = DecisionEngine()

    decision_details = DecisionDetails()
    decision_details.name = details.name
    decision_details.year = details.year

    profit = {}
    for item in details.sheet:
        if item.year in profit:
            profit[item.year] += item.profit_or_loss
        else:
            profit[item.year] = item.profit_or_loss
    
    decision_details.profit = profit

    by_year = {}
    for item in details.sheet:
        if item.year in by_year:
            by_year[item.year][item.month] = item.profit_or_loss
        else:
            by_year[item.year] = {item.month: item.profit_or_loss}

    today = date.today()

    profit_last_12 = 0
    for num in range(1, 13):
        day = today - relativedelta(months=num)
        year = day.year
        month = day.month
        if year in by_year:
            if month in by_year[year]:
                profit_last_12 += by_year[year][month]

    decision_details.preassessment = 20
    if profit_last_12 > 0:
        decision_details.preassessment = 60
    if profit_last_12 > details.amount:
        decision_details.preassessment = 100

    return decision_engine.request(decision_details)
