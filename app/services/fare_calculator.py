from pydantic import ValidationError

from app.schemas import ride_information
import math

from app import config

import logging
logger=logging.getLogger(__name__)

def calculate_base_cost(distance: float, 
                        duration: float,
                        surge_multiplier: float) -> float:
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
            "distance": distance,
            "surge_multiplier":surge_multiplier
        }
        ride_information.FinalCost.model_validate(payload)

        #calculating estimated fare
        floor_distance = math.floor(distance)
        floor_duration = math.floor(duration)
    
        base_cost = config.BASE_FARE + (floor_duration*config.DURATION_RATE) + (floor_distance*config.DISTANCE_RATE)
        final_cost = base_cost * surge_multiplier
        logger.info("Succesfully calculated base cost")

        return final_cost

    except ValidationError:
        logger.exception("Distance/Duration or config data is using an invalid input. Please check again")
        raise