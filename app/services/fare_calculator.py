from pydantic import ValidationError

from app.schemas import ride_information
import math

from app import config

from app.rules.rule_engine import compute_surge_constant

from app.services import search_promo

from datetime import datetime

import logging
logger=logging.getLogger(__name__)

def calculate_base_cost(distance: float, 
                        duration: float) -> float:
    """
    Args:
        distance: the distance from the origin to the destination
        duration: the estimated duration of the whole ride in minutes
    Returns:
        float: the estimated final cost of the ride including the surge multiplier
    Raises:
        ValidationError: an error while trying to validate the input
        Exception: whenever an unexpceted occured
    """
    logger.info(f"Calculating base fare with the distance({distance} and duration({duration}))")
    try:
        #validating input data
        payload = {
            "duration": duration,
            "distance": distance
        }
        ride_information.BaseCost.model_validate(payload)

        #calculating estimated fare
        floor_distance = math.floor(distance)
        floor_duration = math.floor(duration)
    
        base_cost = config.BASE_FARE + (floor_duration*config.DURATION_RATE) + (floor_distance*config.DISTANCE_RATE)

        logger.info("Succesfully calculated base cost")
        return base_cost

    except ValidationError:
        logger.exception("Distance/Duration or config data is using an invalid input. Please check again")
        raise

def calculate_final_fare(distance: float,
                         duration: float,
                         datetime_str: str,
                         demand: int,
                         supply: int,
                         is_airport: bool,
                         partner_cc: bool,
                         promo_name: str = None) -> float:
    dt = datetime.fromisoformat(datetime_str)
    requested_date = dt.date()
    requested_hour = dt.hour
    request_dow = dt.weekday()

    promo_args = {
        "requested_date": requested_date,
        "hour_requested": requested_hour,
        "day_of_week": request_dow,
        "is_airport": is_airport,
        "partner_credit_card": partner_cc
    }
    #calcualte surge multiplier
    surge_multiplier = compute_surge_constant(demand= demand,
                                                supply = supply,
                                                request_time_date=datetime_str)

    #calculate base cost
    base_cost = calculate_base_cost(distance=distance, duration=duration)

    #raw_price
    raw_final_cost = base_cost * surge_multiplier

    #get promo
    promo = search_promo.find_promo(promo_name=promo_name)

    if promo is None:
        return raw_final_cost
    else:
        final_cost = promo.function(raw_final_cost, **promo_args)
        return  final_cost