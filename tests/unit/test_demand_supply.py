import pytest

from app.rules.demand_supply_rules import _compute_demand_supply_ratio, extremely_high_demand, high_demand, moderate_demand, normal_demand

class TestHelperFunc:
    @pytest.mark.parametrize(
        "demand, supply, expected",
        [
            (10,5,2),
            (12,20,0.6),
            (10,10,1),
            (30,6,5)
        ]
    )
    def test_compute_demand_supply_ratio(self, demand, supply, expected):
        test_results = _compute_demand_supply_ratio(demand=demand, supply=supply)

        assert test_results == expected

@pytest.mark.parametrize(
        "demand, supply, expected",
        [
            (10, 5,2.2),
            (20, 3, 2.2),
            (10, 10, None),
            (5, 5, None)
        ]
)
def test_extremely_high_demand(demand, supply, expected):
    test_result = extremely_high_demand(demand=demand, supply=supply)

    assert test_result == expected

@pytest.mark.parametrize(
        "demand, supply, expected",
        [
            (3, 2, 1.8),
            (5, 3, 1.8),
            (10, 5, None),
            (7, 5, None)
        ]
)
def test_high_demand(demand, supply, expected): #
    test_result = high_demand(demand=demand, supply=supply)

    assert test_result == expected

@pytest.mark.parametrize(
        "demand, supply, expected",
        [
            (10, 9, 1.5),
            (4, 3, 1.5),
            (5, 5, None),
            (3, 2, None)
        ]
)
def test_moderate_demand(demand, supply, expected): #
    test_result = moderate_demand(demand=demand, supply=supply)

    assert test_result == expected

@pytest.mark.parametrize(
        "demand, supply, expected",
        [
            (10, 10, 1),
            (12, 30, 1),
            (20, 5, None),
            (12, 10, None)
        ]
)
def test_normal_demand(demand, supply, expected): #
    test_result = normal_demand(demand=demand, supply=supply)

    assert test_result == expected