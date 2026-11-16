from pydantic import BaseModel, Field

from typing import Callable, Optional

class SurgeMultiplierRule(BaseModel):
    name: str
    definition: str
    function: Callable
    active: bool = Field(default=True,
                         description = "if the rule can still be used")
    priority: Optional[int] = Field(
        default=None,
        description = "shows which should be first processed (wherein 1 is most priority)", 
        gt=0)