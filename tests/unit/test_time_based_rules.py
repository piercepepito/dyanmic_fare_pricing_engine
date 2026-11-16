import pytest

from app.rules import time_based_rules

from app import config

class TestTimeBasedRules:
    @pytest.mark.parametrize(
        "datetime_str, expected",
        [
            ("2026-11-16T20:51:00", ("Monday", 20)),
            ("2026-09-22T09:51:00", ("Tuesday", 9)),
            ("2020-04-08T13:51:00", ("Wednesday", 13)),
            ("2000-08-20T05:51:00", ("Sunday", 5)),
        ]
    )
    def test_valid_input(self, datetime_str, expected):
        results = time_based_rules._date_time_extract(datetime_str)

        assert expected == results

    @pytest.mark.parametrize(
        "datetime_str, expected",
        [
            ("2026-11-16T20:51:00", "weekday"),
            ("2026-09-22T09:51:00", "weekday"),
            ("2020-04-08T21:51:00", "weekday"),
            ("2000-08-20T05:51:00", "weekend"),
        ]
    )
    def test_is_weekend(self, datetime_str, expected):
        date_extracted = time_based_rules._date_time_extract(datetime_str)

        result = time_based_rules._is_weekend(date_extracted)

        assert expected == result

    @pytest.mark.parametrize(
        "datetime_str, expected",
        [
            ("2026-11-16T08:51:00", config.IS_RUSH_MULTIPLIER[1]),
            ("2026-09-22T09:51:00", config.IS_RUSH_MULTIPLIER[1]),
            ("2020-04-08T13:51:00", config.IS_RUSH_MULTIPLIER[0]),
            ("2000-08-20T21:51:00", config.IS_RUSH_MULTIPLIER[0]),
        ]
    )
    def test_is_rush_hour(self, datetime_str, expected):
        date_extracted = time_based_rules._date_time_extract(datetime_str)

        result = time_based_rules.is_rush_hour(date_extracted)

        assert expected == result

    @pytest.mark.parametrize(
        "datetime_str, expected",
        [
            ("2026-11-16T08:51:00", config.IS_MALL_CLOSE_MULTIPLIER[0]),
            ("2026-09-22T17:51:00", config.IS_MALL_CLOSE_MULTIPLIER[0]),
            ("2020-04-11T20:51:00", config.IS_MALL_CLOSE_MULTIPLIER[1]),
            ("2000-08-20T21:51:00", config.IS_MALL_CLOSE_MULTIPLIER[1])
        ]
    )
    def test_is_mall_closing(self, datetime_str, expected):
        date_extracted = time_based_rules._date_time_extract(datetime_str)

        result = time_based_rules.is_mall_closing(date_extracted)

        assert expected == result
