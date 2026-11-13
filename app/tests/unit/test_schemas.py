import pytest

from app.schemas import ride_information
from pydantic import ValidationError

class TestRideInfoSchema:
    @pytest.mark.parametrize(
            "field, value",
            [
                ("distance", 0),
                ("duration", -4),
                ("supply", -2),
                ("demand", 0)
            ]
    )
    def test_ride_information_invalid(self, field, value):
        data = {
            "distance": 3,
            "duration":6,
            "demand":20,
            "supply":4,
        }

        data[field] = value
        print(data)
        with pytest.raises(ValidationError):
            ride_information.RideInformation.model_validate(data)