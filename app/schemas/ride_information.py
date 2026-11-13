from pydantic import BaseModel, Field

class BaseCost(BaseModel):
    distance: float = Field(
            description="the distance between the origin and the destination",
            gt=0)
    duration: float = Field(
            description="an estimated duration of the whole ride",
            gt=0)

class FinalCost(BaseCost):
    surge_multiplier: float = Field(description= "a multiplier taking into account the supply and demand dependent on the pick up zone", 
                                    ge=1)

class RideInformation(BaseCost):
    supply: int = Field(
            description="number of drivers roaming around an area from the origin",
            gt=0)
    demand: int = Field(
            description="number of people waiting in the pick up zone",
            gt=0)    
