from fastapi import Depends, FastAPI
from app.routers import accounting, decision, initiate

app = FastAPI()

app.include_router(initiate.router)
app.include_router(accounting.router)
app.include_router(decision.router)
