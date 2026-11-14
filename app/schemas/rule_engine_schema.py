from pydantic import BaseModel, Field

from typing import Callable

class SurgeMultiplierRule(BaseModel):
    name: str
    definition: str
    function: Callable
    active: bool = Field(default=True,
                         description = "if the rule can still be used")
    priority: int = Field(description = "shows which should be first processed", gt=0)