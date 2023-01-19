import pytest

from utils import all_information, day_category


def test_all_information():
    info = all_information()
    assert info[0]["departure"] == "0:10", 'Функция возвращает неверную информацию'


def test_day_category(day):
    info = day_category(day)
    assert info[0] == {'departure': '3:51', 'arrival': '4:12', 'station': 'Захарово', 'days': 'вых.', 'halt': 'кр. Серп и Молот, Карачарово, Чухлинка, Кусково, Новогиреево, Никольское, Салт., Кучино'}, 'Поиск по типу дня неверный'


def station(name_st):
    info = station(name_st)
    assert info[1] == {'departure': '4:45', 'arrival': '5:19', 'station': 'Захарово', 'days': 'раб.', 'halt': 'везде'}, 'Поиск по названию станции выполняется неверно'

