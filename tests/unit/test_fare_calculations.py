from pydantic import ValidationError

import pytest
from unittest.mock import Mock, patch

from app.services import fare_calculator

class TestBaseCost:
    @pytest.mark.parametrize(
            "distance, duration, expected",
            [
                (5, 15, 162.5), #purely integers
                (2.7, 3.65, 98), #all floating
                (3.34, 15, 135.5) #mix between float and integer
            ]
    )
    def test_valid_input(self, distance, duration, expected):
        test_result = fare_calculator.calculate_base_cost(
            distance=distance,
            duration=duration
        )

        assert test_result == expected

    @pytest.mark.parametrize(
            "duration, distance",
            [
                (-0.1, 2),
                (3,-4),
                (0, -1),
                (-1, 2.13),
                (4, 0)
            ]
    )
    def test_invalid_input(self, duration, distance):
        with pytest.raises(ValidationError):
            fare_calculator.calculate_base_cost(
                distance = distance,
                duration = duration
                )
