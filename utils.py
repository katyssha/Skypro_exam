import json
import os


def all_information():
    """Загружает всю информацию из data1.json"""
    with open(os.path.join('data', 'data1.json'), 'r', encoding='utf-8') as f:
        schedule = json.load(f)
    return schedule


def day_category(day):
    """Поиск по типу дня(вых., ежедн. и тд)"""
    schedule = all_information()
    days = []
    for inf in schedule:
        if inf['days'] == day:
            days.append(inf)
    return days

def station(name_st):
    """Поиск по названию станции"""
    schedule = all_information()
    stations = []
    for inf in schedule:
        if inf['station'] == name_st:
            stations.append(inf)
    return stations

