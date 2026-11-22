from app.cache import cache_service, redis_client
from app.services import create_hash

import redis

import pytest
from unittest.mock import Mock, patch

class TestCreateCache:
    @pytest.mark.parametrize(
            "fare_input",
            [
                ({"fare": 320, "datetime_request":"2026-11-10"}),
                ({"is_cc": True, "fare": 950}),
                ({"is_airport":True, "date_request":"2025-11-22"})
            ]
    )
    def test_valid_input(self, fare_input):
        cache_result = 320
        hash_key = create_hash.create_hash(fare_input=fare_input)

        result = cache_service.create_cache(prefix="fare",
                                            cache_key=hash_key,
                                            value=cache_result,
                                            ttl=300)

        assert result == True

        #retrieve
        cache_key=f"fare:{hash_key}"
        retrieved_result = int(redis_client.redis_cache.get(cache_key))

        assert retrieved_result == cache_result

    @patch("app.cache.cache_service.redis_client")
    def test_redis_error(self, mock_redis_client):
        mock_redis_client.redis_cache.set.side_effect = redis.exceptions.RedisError

        result = cache_service.create_cache(prefix="fare",
                                            cache_key="some-fake-key",
                                            value=200,
                                            ttl=100)

        assert result == False

class TestRetrieveCache:
    @pytest.mark.parametrize(
            "value",
            [
                320,
                500,
                600,
                728
            ]
    )
    def test_valid_input(self, value, ttl=100):
        fare_input={"fare": 720, "datetime_req":"2026-08-10"}
        hash_key = create_hash.create_hash(fare_input=fare_input)

        cache_service.create_cache(prefix="fare", cache_key=hash_key, 
                                   value=value, ttl=ttl)

        result = int(cache_service.pull_cache(prefix="fare", 
                                              cache_key=hash_key))

        assert result == value

    @patch("app.cache.cache_service.redis_client")
    def test_redis_error(self, mock_redis_client):
        mock_redis_client.redis_cache.get.side_effect = redis.exceptions.RedisError("An error occured while connecting to Redis")

        result = cache_service.pull_cache(prefix="fare",
                                          cache_key="some-key")

        assert result == None



        