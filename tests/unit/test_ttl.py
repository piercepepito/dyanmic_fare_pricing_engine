from app.cache import ttl
from app import config

from datetime import time

import pytest

class TestTTLCompute:
    @pytest.mark.parametrize(
            "time_start, expected",
            [
                (time(15, 59, 30), 30), #rush hour morning
                (time(6,59, 0), 60), #rush hour afternooon
                (time(14, 0, 0), config.max_ttl), #between 2 rush hours
                (time(20, 0, 0), config.max_ttl), #evening time
                (time(3,0,0), config.max_ttl) #early morning
            ]
    )
    def test_ttl_compute(self, time_start, expected):
        result = ttl.ttl_compute(request_time=time_start)

        assert result == expected