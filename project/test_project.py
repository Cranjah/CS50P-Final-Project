#!/usr/bin/env python3

# import pytest
from random import Random
# from project import func1, func2, func3, func4, func5, func6


def test_random():
    random = Random(666)
    assert random.randint(0, 1000) == 467


"""
def test_func1():
    assert func1("") == ""
    assert func1("") == ""
    assert func1("") == ""

def test_func2():
    assert func2("") == ""
    assert func2("") == ""
    assert func2("") == ""

def test_func3():
    assert func3("") == ""
    assert func3("") == ""
    assert func3("") == ""

    ...
"""

# CMD: pip install pytest
