"""
Тесты на ДЗ#5.
"""

import datetime

from hw5_solution1 import Person


def tests_for_hw5_solution1():
    """Тесты задачи 1"""
    petroff = Person("Petrov", "Petro", "1952-01-02")
    ivanoff = Person("Ivanov", "Ivan", "2000-10-20")
    sydoroff = Person("Sidorov", "Semen", "1980-12-31", "Senya")

    assert "first_name" in dir(petroff)
    assert "get_fullname" in dir(ivanoff)
    assert "nickname" not in dir(petroff)
    assert "nickname" in dir(sydoroff)

    assert petroff.surname == "Petrov"
    assert petroff.first_name == "Petro"
    assert petroff.get_fullname() == "Petrov Petro"
    assert sydoroff.nickname == "Senya"

    assert petroff.birth_date == datetime.date(1952, 1, 2)
    assert isinstance(petroff.birth_date, datetime.date)
    assert petroff.get_age() == "64"

    print('All is Ok!')