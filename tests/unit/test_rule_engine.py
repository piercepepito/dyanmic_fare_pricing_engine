import pytest

from app.rules import rule_engine
from app import config

class TestDemandSupplyEngine:
    @pytest.mark.parametrize(
            "demand, supply, expected",
            [
                (20, 3, 2.2),
                (35, 18, 1.8),
                (20, 19, 1.5),
                (5,5, 1)
            ]
    )
    def test_valid_inputs_demand_supply(self, demand, supply, expected):
        test_result = rule_engine.rule_engine_demand_supply(demand=demand,
                                                            supply=supply)

        assert expected == test_result

class TestTimeBasedEngine:
    @pytest.mark.parametrize(
        "datetime_str, expected",
        [
            ("2026-11-16T08:51:00", config.IS_RUSH_MULTIPLIER[1]),
            ("2026-09-22T09:51:00", config.IS_RUSH_MULTIPLIER[1]),
            ("2020-04-08T13:51:00", config.IS_RUSH_MULTIPLIER[0]),
            ("2000-08-20T19:51:00", config.IS_RUSH_MULTIPLIER[0]),
            ("2026-11-16T11:51:00", config.IS_MALL_CLOSE_MULTIPLIER[0]),
            ("2026-09-22T21:51:00", config.IS_MALL_CLOSE_MULTIPLIER[0]),
            ("2020-04-11T20:51:00", config.IS_MALL_CLOSE_MULTIPLIER[1]),
            ("2000-08-20T21:51:00", config.IS_MALL_CLOSE_MULTIPLIER[1])
        ]
    )
    def test_valid_inputs_time_based(self, datetime_str, expected):
        
        result = rule_engine.rule_engine_time_based(datetime_str)

        assert expected == result

