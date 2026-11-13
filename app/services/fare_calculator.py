from pydantic import ValidationError

from app.schemas import ride_information

from app import config

import logging
logger=logging.getLogger(__name__)

def calculate_base_cost(distance: float, 
                        duration: float) -> float:
    """
    Args:
        distance: the distance from the origin to the destination
        duration: the estimated duration of the whole ride
    Returns:
        float: the estimated base cost of the ride
    Raises:
        ValidationError: an error while trying to validate the input
        Exception: whenever an unexpceted occured
    """
    logger.info(f"Calculating base fare with the distance({distance} and duration({duration}))")
    payload = {
        "duration":duration,
        "distance": distance
    }
    ride_information.BaseCost.model_validate(payload)

    try:
        base_cost = config.BASE_FARE + (duration*config.DURATION_RATE) + (distance*config.DISTANCE_RATE)
        logger.info("Succesfully calculated base cost")
        return base_cost

    except ValidationError:
        logger.exception("Distance/Duration is using an invalid input. Please check again")
        raise
