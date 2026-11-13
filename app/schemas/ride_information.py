from pydantic import BaseModel, Field


class RideInformation(BaseModel):
    distance: int = Field(
            description="the distance between the origin and the destination",
            gt=0)
    duration: int = Field(
            description="an estimated duration of the whole ride",
            gt=0)
    supply: int = Field(
            description="number of drivers roaming around an area from the origin",
            gt=0)
    demand: int = Field(
            description="number of people waiting in the pick up zone",
            gt=0)
    
