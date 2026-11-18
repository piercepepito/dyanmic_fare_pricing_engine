from app.rules import demand_supply_rules, time_based_rules
from app.schemas import rule_engine_schema

import math

from datetime import datetime

def rule_engine_demand_supply(demand: int, 
                              supply: int,
                              pricing_rules: list = demand_supply_rules.PRICING_RULES)-> float|None:
    """
    A rule prioritization method that loops around all possible demand and supply rules, and stops when the condition has been met
    Args:
        demand: number of passengers in that area
        supply: the number of drivers in the area
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

def rule_engine_time_based(request_date_time: str,
                           time_rules: list[rule_engine_schema.SurgeMultiplierRule] = time_based_rules.TIME_BASED_PRICING
                           ) -> float:
   """
   Checks multiple time based rules, gets the product of all multipliers that have a sucecsful condition

   Args:
    request_date_time: the date and time request when the endpoint has been called with the proper datetime format
   Returns:
    float: the product of all multipliers where the condition has been satisfied
   """ 
   extracted_datetime = time_based_rules.date_time_extract(request_date_time)

   multipliers = []
   for rule in time_rules:
       time_multiplier = rule.function(extracted_datetime)
       if time_multiplier != None:
        multipliers.append(time_multiplier)

   surge_multiplier = math.prod(multipliers)
   return surge_multiplier

def compute_surge_constant(demand: int, 
                   supply: int,
                   request_time_date: str,
                   MIN_SURGE_MULTIPLIER: int=1,
                   MAX_SURGE_MULTIPLIER: int=2.5) -> float:
   """
   Multiplies both surge multipliers from time based and demand supply. A guard clause is created that makes sure that the 
   output would never go below 1.

   Args:
        demand: number of passengers in that area
        supply: the number of drivers in the area
        request_time_date: the GET request timestamp
    Returns:
        final_surge_mult: the product between demand_supply and time_based
   """
   demand_supply_multiplier = rule_engine_demand_supply(demand=demand, supply=supply)
   time_based_multiplier = rule_engine_time_based(request_date_time=request_time_date)

   #clamping
   raw_surge_mult = demand_supply_multiplier * time_based_multiplier
   normalize_surge = max(MIN_SURGE_MULTIPLIER, raw_surge_mult)

   return MAX_SURGE_MULTIPLIER if normalize_surge > MAX_SURGE_MULTIPLIER else normalize_surge