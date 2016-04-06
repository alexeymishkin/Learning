# -*- coding: utf8 -*-

"""
Тесты на ДЗ#2.
"""

import hw4


def tests_for_hw4_solution1():
    u"""Тесты задачи 1"""
    assert hw4.percentage("A") == {'a': 100.0}
    assert hw4.percentage("ABCda") == {
        'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0
    }
    assert hw4.percentage("AsBCda") == {
        'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7
    }
    assert hw4.percentage("q TyU#!.") == {
        'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0
    }
    assert sum(hw4.percentage("q TyU#!.").values()) == 100.0



def tests_for_hw4_solution2():
    u"""Тесты задачи 2"""
    text = "Proin eget tortor risus."
    assert hw4.ellipsis_1(text) == "Proin eget tortor risus."
    assert hw4.ellipsis_1(text, 24) == "Proin eget tortor risus."
    assert hw4.ellipsis_1(text, 23) == "Proin eget tortor..."
    assert hw4.ellipsis_1(text, 13) == "Proin eget..."
    assert hw4.ellipsis_1(text, 3)  == "Pro..."


tests_for_hw4_solution1()
tests_for_hw4_solution2()