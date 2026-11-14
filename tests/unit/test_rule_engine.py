import pytest

from app.rules import rule_engine

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
    def test_valid_inputs(self, demand, supply, expected):
        test_result = rule_engine.rule_engine_demand_supply(demand=demand,
                                                            supply=supply)

        assert expected == test_result

