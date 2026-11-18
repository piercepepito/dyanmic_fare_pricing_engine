from pydantic import BaseModel, Field

from typing import Callable, Optional, Literal

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

class PromoRule(SurgeMultiplierRule):
    promo_type: Literal["flat_fee", "percentage"] = Field(
            default=None,
            description="used to check type of promo which can either be a flat fee or a percentage discount"
        )
    promo_num: float = Field(
        description = "the number that should be subtracted or product of the total",
        gt = 0
    )