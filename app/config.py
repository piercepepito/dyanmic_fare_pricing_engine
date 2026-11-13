#base fare calculations
BASE_FARE=65
DURATION_RATE=2
DISTANCE_RATE=13.5

#config data validation
def config_data_validation():
    if BASE_FARE <= 0:
        raise ValueError("Base fare should be greater than 0")
    if DURATION_RATE <= 0:
        raise ValueError("Duration rate should be greater than 0")
    if DISTANCE_RATE <= 0:
        raise ValueError("Distance rate should be greater than 0")

config_data_validation()