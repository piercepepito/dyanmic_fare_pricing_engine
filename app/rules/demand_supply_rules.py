import logging
logger = logging.getLogger(__name__)

from app import config
from app.schemas.rule_engine_schema import SurgeMultiplierRule

def _compute_demand_supply_ratio(demand: int, supply: int) -> float:
    """
    Computes the ratio between the demand and supply of that current pick up zone

    Args:
        demand: the number of passengers within that area
        supply: The number of drivers within the area
    Returns:
        float: the ratio between the demand and supply
    """
    return demand/supply

#computes and categorizes the demand-supply ratio
def extremely_high_demand(demand, supply) -> float|None:
    """
    Returns the EXTREMELY HIGH demand multiplier if the threshold is met
    """ 
    ratio = _compute_demand_supply_ratio(demand=demand, supply=supply)
    if ratio >= config.EXTREMELY_HIGH_DEMAND_THRESHOLD:
        return config.EXTREMELY_HIGH_DEMAND

def high_demand(demand, supply) -> float|None:
    """
    Returns HIGH demand multiplier if the threshold is met
    """ 
    ratio = _compute_demand_supply_ratio(demand=demand, supply=supply)
    if (ratio >= config.HIGH_DEMAND_THRESHOLD[0]) and (ratio < config.HIGH_DEMAND_THRESHOLD[1]):
        return config.HIGH_DEMAND

def moderate_demand(demand, supply) -> float|None:
    """
    Returns the MODERATE demand multiplier if the threshold is met
    """ 
    ratio = _compute_demand_supply_ratio(demand=demand, supply=supply)
    if (ratio > config.MODERATE_DEMAND_THRESHOLD[0]) and (ratio < config.MODERATE_DEMAND_THRESHOLD[1]):
        return config.MODERATE_DEMAND

def normal_demand(demand, supply) -> float|None:
    """
    Returns the NORMAL demand multiplier if the threshold is met
    """ 
    ratio = _compute_demand_supply_ratio(demand=demand, supply=supply)
    if (ratio <= config.NORMAL_DEMAND_THRESHOLD):
        return config.NORMAL_DEMAND

#define the pricing rules
PRICING_RULES = [
    SurgeMultiplierRule(
        name = "extremely high demand",
        definition = "if the demand far exceeds the supply",
        function = extremely_high_demand,
        active=True,
        priority = 1
    ),
    SurgeMultiplierRule(
        name = "high demand",
        definition = "The demand is higher than expected compared to the supply",
        function = high_demand,
        active = True,
        priority = 2
    ),
    SurgeMultiplierRule(
        name = "moderate demand",
        definition = "The demand is slightly just above 1",
        function = moderate_demand,
        active = True,
        priority = 3
    ),
    SurgeMultiplierRule(
        name = "normal demand",
        definition = "When the demand is equal or less than the supply",
        function = normal_demand,
        active=True,
        priority=4
    )
]


if __name__=="__main__":
    yeah = sorted(PRICING_RULES, key = lambda x: x.priority)

    filtered = [u for u in PRICING_RULES if u.active == True]

    for cool in filtered:
        print(cool)

