from app.rules import demand_supply_rules

def rule_engine_demand_supply(demand: int, 
                              supply: int,
                              pricing_rules: list = demand_supply_rules.PRICING_RULES)-> float|None:
    """
    A rule prioritization method that loops around all possible demand and supply rules, and stops when the condition has been met
    Args:
        pricing_rules: a list of all 
    Returns:
        a surge multiplier defined from the demand and supply py
    """
    filtered_pricing_rules = [u for u in pricing_rules if u.active == True]
    sorted_pricing_rules = sorted(filtered_pricing_rules, key=lambda x: x.priority)
    
    for rule in sorted_pricing_rules:
        surge_multiplier = rule.function(demand=demand, supply=supply)

        if surge_multiplier is not None:
            return surge_multiplier