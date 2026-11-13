from pydantic import ValidationError

import pytest
from unittest.mock import Mock, patch

from app.services import fare_calculator

class TestBaseCost:
    @pytest.mark.parametrize(
            "distance, duration, multiplier, expected",
            [
                (5, 15, 1.23, 199.875), #purely integers
                (2.7, 3.65, 1.76, 172.48), #all floating
                (3.34, 15, 1.99, 269.645) #mix between float and integer
            ]
    )
    def test_valid_input(self, distance, duration, multiplier, expected):
        test_result = fare_calculator.calculate_base_cost(
            distance=distance,
            duration=duration,
            surge_multiplier=multiplier
        )

        assert test_result == expected

    @pytest.mark.parametrize(
            "duration, distance, multiplier",
            [
                (-0.1, 2, 1),
                (3,-4, 1.22),
                (0, -1, 3.12),
                (1, 2.13, 0.5),
                (4, 3.32, 0.99)
            ]
    )
    def test_invalid_input(self, duration, distance, multiplier):
        with pytest.raises(ValidationError):
            fare_calculator.calculate_base_cost(
                distance = distance,
                duration = duration,
                surge_multiplier = multiplier
                )
