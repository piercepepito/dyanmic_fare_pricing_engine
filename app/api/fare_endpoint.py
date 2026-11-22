from fastapi import APIRouter, status

from app.schemas import fare_schema

from app.services import fare_calculator

router=APIRouter()

@router.post("/calculate-fare",
             status_code=status.HTTP_201_CREATED,
             response_model=fare_schema.FareResponse)
def calculate_fare_endpoint(fare_request: fare_schema.FareRequest):
    fare_price = fare_calculator.get_fare(fare_request)

    fare_response = {
        "total_fare":fare_price
    } 
    return fare_response