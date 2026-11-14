import logging
logger = logging.getLogger(__name__)

from app import config

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