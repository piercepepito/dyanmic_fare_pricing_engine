from app.schemas.rule_engine_schema import PromoRule

from app.rules import time_based_rules

from datetime import datetime, date

def mid_day_promo(raw_final_price, **kwargs):
    within_time_zone =  10 <= kwargs["hour_requested"] <= 15
    is_weekday = 0 <= kwargs["day_of_week"] < 5

    mid_day_condition = [within_time_zone, is_weekday]

    if all(mid_day_condition):
        discounted_price = raw_final_price*0.2

        final_price = (raw_final_price - 80) if discounted_price >= 80 else (raw_final_price - discounted_price)
    else:
        raise ValueError("Time of day does notsatisfy conditions for the promo.")
    
    return final_price

def fly_away_promo(raw_final_price, **kwargs):
    if kwargs["is_airport"]:
        final_price = raw_final_price - 200
        return max(0, final_price)
    else:
        raise ValueError("Destination/Origin is not the airport.")

def wallet_save_promo(raw_final_price, **kwargs):
    if kwargs["partner_credit_card"]:
        return (raw_final_price*0.75)
    else:
        raise ValueError("Card used is not a partner credit card")

def love_delivered_promo(raw_final_price, **kwargs):
    is_valentines_weekend =  date(2026, 2, 13) <= kwargs["requested_date"] <= date(2026, 2, 15)

    if is_valentines_weekend:
        init_discount_price = raw_final_price*0.2
        discounted_price = 143 if  init_discount_price >= 143 else init_discount_price

        return raw_final_price - discounted_price
    else:
        raise ValueError("Requested date is still not part of the Valentine's day Weekend")



PROMO_RULES = [
    PromoRule(
        name = "MIDDAY20",
        definition = "Enjoy 20% off rides booked between 10:00 AM and 3:00 PM. Valid Monday through Friday. Maximum discount of ₱80 per trip.",
        function = mid_day_promo,
        active = True,
        promo_type = "flat_fee",
        promo_num = 80
    ),
    PromoRule(
        name = "FLYAWAY",
        definition = "₱200 off trips going to or from major international and domestic airports.",
        function=fly_away_promo,
        active=True,
        promo_type="flat_fee",
        promo_num=200
    ),
    PromoRule(
        name="WALLETSAVE",
        definition="Get 15% off your ride when paying with a partner credit card.",
        function=wallet_save_promo,
        active=True,
        promo_type="percentage",
        promo_num=0.15
    ),
    PromoRule(
        name="LOVEDELIVERED",
        definition="Get 20% off (up to ₱143 off per ride) when heading out for Valentine’s weekend (February 13 to 15).",
        function = love_delivered_promo,
        active=False,
        promo_type="percentage",
        promo_num=0.2
    )
    ]