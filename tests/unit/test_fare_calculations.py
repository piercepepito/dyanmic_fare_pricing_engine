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

class TestFinalCost:
    @pytest.mark.parametrize(
            "distance, duration, datetime_str, demand, supply, is_airport, partner_cc, promo_name, expected",
            [
                (5,15,"2026-11-16T08:51:00",20,3,False,False,None,406.25),
                (2.7,3.65,"2020-04-08T13:51:00",35,18,False,False,None,176.4),
                (2.7,3.65,"2020-04-08T13:51:00",35,18,False,False,"FAKE PROMO",176.4), #used a fake promo_name
                (2.7,3.65,"2020-04-08T13:51:00",35,18,False,False,"MIDDAY20",141.12), #used a promo
                (2.7,3.65,"2020-04-08T13:51:00",35,18,True,False,"FLYAWAY",0) #used a promo
            ]
    )
    def test_valid_inputs(self,
                            distance,
                            duration,
                            datetime_str,
                            demand,
                            supply,
                            is_airport,
                            partner_cc,
                            promo_name,
                            expected):
        
        result = fare_calculator.calculate_final_fare(
            distance = distance,
            duration = duration,
            datetime_str = datetime_str,
            demand = demand,
            supply = supply,
            is_airport = is_airport,
            partner_cc = partner_cc,
            promo_name = promo_name
        )

        assert result == expected