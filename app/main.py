import logging

from fastapi import FastAPI
from app.api.fare_endpoint import router as fare_router

app = FastAPI(
    title="Dyanmic Fare Calculator",
    description="calcualtes the fare for a simulated hail riding comapny",
    version="1.0.0"
)

app.include_router(fare_router)

