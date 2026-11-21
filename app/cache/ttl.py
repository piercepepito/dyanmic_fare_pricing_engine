from datetime import datetime, time

from app import config

def _datetime_diff(end: datetime, start: datetime) -> int:
    """
    Args:
        start:
        end: 
    Returns:
        int: the difference between two dates in seconds
    """
    return (end-start).total_seconds()


def ttl_compute(request_time: time, 
                max_ttl: int = config.max_ttl) -> int:
    """
    Computes the ttl needed for cache invalidation

    Args:
        start: the request of the datetime
        max_ttl: the max ttl limit whenever the computed ttl goes above a threshold
    Returns:
        float: the ttl of cached key
    """
    #define the date today
    date_today = datetime.today()
    #define the start_date
    start_date = datetime.combine(date_today, request_time)
    #define the start of the rush hour
    rush_hour_morning_start=time(config.IS_RUSH_HOUR_MORNING[0],0,0)
    rush_hour_afternoon_start=time(config.IS_RUSH_HOUR_AFTERNOON[0],0,0)

    rush_hour = [datetime.combine(date_today, rush_hour_morning_start), 
             datetime.combine(date_today, rush_hour_afternoon_start)]

    time_diff = [_datetime_diff(end=rush_hour_time, start=start_date) for rush_hour_time in rush_hour 
                 if 0 <= _datetime_diff(end=rush_hour_time, start=start_date) <= max_ttl]

    if len(time_diff) != 0:
        ttl_computed = time_diff[0]
    else:
        ttl_computed = abs(_datetime_diff(end=date_today, start=start_date))

    return int(min(ttl_computed, max_ttl))