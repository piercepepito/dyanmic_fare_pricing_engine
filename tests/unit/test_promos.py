import pytest

from app.rules import promos

from datetime import datetime

class TestPromoFunctions:
    @pytest.mark.parametrize(
        "raw_final_price, hour_requested, day_of_week, expected",
        [
            (180, 11, 3, 144),
            (550, 14, 2, 470),
            (300, 2, 3, ValueError)
        ]
    )
    def test_mid_day_promo(self,
                           raw_final_price, 
                           hour_requested, 
                           day_of_week, 
                           expected):
        promo_data = {
            "requested_date":None,
            "hour_requested": hour_requested,
            "day_of_week": day_of_week,
            "is_airport": None,
            "partner_credit_card": None
        }
        try:
            result = promos.mid_day_promo(raw_final_price = raw_final_price, 
                                        **promo_data)

            assert expected == result
        except Exception:
            assert ValueError == expected

    @pytest.mark.parametrize(
            "is_airport, raw_final_price, expected",
            [
                (True, 650, 450),
                (True, 180, 0),
                (False, 480, ValueError)
            ]
    )
    def test_fly_away(self, is_airport, raw_final_price, expected):
        promo_data = {
                    "requested_date":None,
                    "hour_requested": None,
                    "day_of_week": None,
                    "is_airport": is_airport,
                    "partner_credit_card": None
                }
        try:
            result = promos.fly_away_promo(raw_final_price=raw_final_price,
                                        **promo_data)
            assert result == expected
        except Exception:
            assert ValueError == expected

    @pytest.mark.parametrize(
            "raw_final_price, is_partner_cc, expected",
            [
                (100, True, 75),
                (200, True, 150),
                (100, False, ValueError)
            ]
    )
    def test_wallet_save(self, raw_final_price, is_partner_cc, expected):
        try:
            result = promos.wallet_save_promo(raw_final_price=raw_final_price,
                                            partner_credit_card=is_partner_cc)

            assert result == expected
        except Exception:
            assert ValueError == expected
    @pytest.mark.parametrize(
            "raw_final_price, requested_date, expected",
            [
                (500 ,"2026-02-14T20:51:00", 400),
                (1350, "2026-02-15T20:51:00", 1207),
                (1920, "2026-02-23T20:51:00", ValueError)
            ]
    )
    def test_love_delivered_promo(self, raw_final_price, 
                             requested_date, expected):
        datetime_requested_date = datetime.fromisoformat(requested_date).date()

        try:
            result = promos.love_delivered_promo(raw_final_price=raw_final_price,
                                                requested_date=datetime_requested_date)

            assert expected == result
        except Exception:
            assert ValueError == expected