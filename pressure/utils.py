from .models import BloodPressure


def average_pressure(pressure_list: list) -> int:
    if not pressure_list:
        return 0
    avr = round(sum(pressure_list)/len(pressure_list))
    return avr


def last_month_year(user)->tuple:
    last_entry = BloodPressure.objects.filter(user=user)[0]
    return (last_entry.created.year, last_entry.created.month)