from datetime import datetime
from typing import Literal

from app import config

from app.schemas.rule_engine_schema import SurgeMultiplierRule

day_of_week_name = Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def date_time_extract(date_time: str) -> tuple[str, int]:
    """
    Extracting the day of the week and the hour, based on the datetime input

    Args:
        date_time: a text that would have a date time format 
    Returns:
        - the name of the day in a week (e.g. Saturday, Sunday)
        - the hours of the day (from 0 to 24)
    """
    date_time_convert = datetime.fromisoformat(date_time)

    return date_time_convert.strftime("%A"), date_time_convert.hour

#date time rules
def _is_weekend(extracted_date_time: tuple[day_of_week_name, int]) -> float:
    """
    Checks if the day of the week is a weekend or not

    Args:
        extracted_date_time: returned data from the date_time_extract func. Only the 1st element of the tuple will be used
    Returns:
        float: a surge multiplier if left True, otherwise it would return None
    """
    day_week_name = extracted_date_time[0]
    if (day_week_name == "Saturday") or (day_week_name == "Sunday"):
        return "weekend"
    else:
        return "weekday"

def is_rush_hour(extracted_date_time: tuple[day_of_week_name, int]) -> float:
    """
    Checks if the hour of the day is during a rush hour, which is only applicable during a weekday

    Args:
        extracted_date_time: returned data from the date_time_extract func. Only the 2nd element of the tuple will be used
    Returns:
        float: a surge multiplier if left True, otherwise it would return None
    """
    weekday_condition = True if _is_weekend(extracted_date_time=extracted_date_time) == "weekday" else False

    hour_of_day = extracted_date_time[1]

    morning_rush = config.IS_RUSH_HOUR_MORNING[0] <= hour_of_day <= config.IS_RUSH_HOUR_MORNING[1]  #returns bool
    afternoon_rush = config.IS_RUSH_HOUR_AFTERNOON[0] <= hour_of_day <= config.IS_RUSH_HOUR_AFTERNOON[1] #returns bool

    rush_conditions = any([morning_rush, afternoon_rush])
    conditions = all([rush_conditions, weekday_condition])

    rush_hour = config.IS_RUSH_MULTIPLIER[1] if conditions else config.IS_RUSH_MULTIPLIER[0]
    return rush_hour

def is_mall_closing(extracted_date_time: tuple[day_of_week_name, int]) -> bool:
    """
    Checks if the hour of the day is during opening/closing mall hours. Only available during weekends.

    Args:
        extracted_date_time: returned data from the date_time_extract func. Only the 2nd element of the tuple will be used
    Returns:
        float: a surge multiplier if left True, otherwise it would return None

    """
    weekend_condition = True if _is_weekend(extracted_date_time=extracted_date_time) == "weekend" else False

    hour_of_day = extracted_date_time[1]

    closing_time = config.IS_MALL_CLOSING[0] <= hour_of_day <= config.IS_MALL_CLOSING[1] #military time

    conditions = all([weekend_condition, closing_time])    

    mall_multiplier = config.IS_MALL_CLOSE_MULTIPLIER[1] if conditions else config.IS_MALL_CLOSE_MULTIPLIER[0] 
    return mall_multiplier

TIME_BASED_PRICING = [
    SurgeMultiplierRule(
        name = "is rush hour",
        definition = "checks if the hour of the day is during rush hour",
        function = is_rush_hour,
        active = True
    ),
    SurgeMultiplierRule(
        name="is mall closing",
        definition = "checks if the hour is during mall closing hours",
        function = is_mall_closing,
        active=True
    )
]