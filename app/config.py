#base fare calculations
BASE_FARE=65
DURATION_RATE=2
DISTANCE_RATE=13.5

#demand and supply threshold
EXTREMELY_HIGH_DEMAND_THRESHOLD = 2
HIGH_DEMAND_THRESHOLD = (1.5, 2)
MODERATE_DEMAND_THRESHOLD = (1, 1.5)
NORMAL_DEMAND_THRESHOLD = 1

#demand and supply multipliers
EXTREMELY_HIGH_DEMAND = 2.2 
HIGH_DEMAND = 1.8
MODERATE_DEMAND = 1.5 
NORMAL_DEMAND = 1

#time based multipliers
IS_RUSH_HOUR_MORNING = (7,9)
IS_RUSH_HOUR_AFTERNOON = (16,20)
IS_RUSH_MULTIPLIER = (1, 1.8)

IS_MALL_CLOSING = (20, 22)
IS_MALL_CLOSE_MULTIPLIER = (1, 1.7)

#config data validation
def config_data_validation():
    if BASE_FARE <= 0:
        raise ValueError("Base fare should be greater than 0")
    if DURATION_RATE <= 0:
        raise ValueError("Duration rate should be greater than 0")
    if DISTANCE_RATE <= 0:
        raise ValueError("Distance rate should be greater than 0")

config_data_validation()