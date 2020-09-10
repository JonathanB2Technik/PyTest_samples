import math_func
import pytest
import sys


def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9


def test_multiply():
    assert math_func.multiply(7, 3) == 21
    assert math_func.multiply(7) == 14


def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36


def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result
    print('--------------', math_func.add('Hello ', 'World'), '--------------')


def test_multiply_strings():
    assert math_func.multiply('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.multiply('Hello ')
    assert  result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
