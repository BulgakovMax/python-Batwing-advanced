import pytest
from functions_to_test import Calculator

def test_add():
    assert Calculator.add(2, 0) == 2
    assert Calculator.add(-2, -2) == -4

def test_substract():
    assert Calculator.subtract(2, 0) == 2
    assert Calculator.subtract(-2, -2) == 0

def test_multiply():
    assert Calculator.multiply(2, 0) == 0
    assert Calculator.multiply(-2, -2) == 4

def test_divide():
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
    assert Calculator.divide(-2, -2) == 1