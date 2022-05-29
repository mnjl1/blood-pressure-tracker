from .models import BloodPressure


def average_pressure(pressure_list: list) -> int:
    if not pressure_list:
        return 0
    avr = round(sum(pressure_list)/len(pressure_list))
    return avr
