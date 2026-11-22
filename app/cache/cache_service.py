from app.cache import redis_client

import redis

import logging

logger = logging.getLogger(__name__)

def create_cache(prefix: str, cache_key: str, value: int, ttl: int)-> bool:
    """
    Creates cache, from the key provided

    Args:
        prefix: the prefix added to the cache key
        cache_key: a hexadecimal string with a hashed input from the fare input dict
        value: the value to be set for the cache
        ttl: expiry time in seconds for the cache
    Returns:
        bool: returns True if cache has been succesfully created
    """
    try:
        cache_key = f"{prefix}:{cache_key}"

        redis_client.redis_cache.set(cache_key, value, ex=ttl)

        logging.info(f"Succesfully created cache with cache_key: {cache_key}")
        return True

    except redis.exceptions.RedisError as e:
        logging.warning(f"A Redis error while creating cache: {str(e)}")
        return False

def pull_cache(prefix: str, cache_key: str) -> int|None:
    """
    Retrieves the cache from the cache key

    Args:
        prefix: the prefix added to the cache key
        cache_key: a hexadecimal string with a hashed input from the fare input dict
    Returns:
        int|None: the fare value, but if there is no matching cache key then it returns None
    """
    try:
        cache_key = f"{prefix}:{cache_key}"

        cached_value = redis_client.redis_cache.get(cache_key)

        logging.info(f"Succesfully retrieved cache value with cache_key: {cache_key}")
        return cached_value
    
    except redis.exceptions.RedisError as e:
        logging.warning(f"Redis pull cache value failed {e}")
        return None