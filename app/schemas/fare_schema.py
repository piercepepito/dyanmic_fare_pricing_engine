from pydantic import BaseModel, Field

class FareRequest(BaseModel):
    distance: float = Field(gt=0)
    duration: float = Field(gt=0)
    datetime_str: str
    demand: int = Field(gt=0)
    supply: int = Field(gt=0)
    is_airport: bool
    partner_cc: bool
    promo_name: str|None = None

class FareResponse(BaseModel):
    total_fare: float = Field(gt=0)