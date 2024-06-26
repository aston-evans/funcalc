

import pytest

from funcalc.calc import addition, division, multiplication, slow_division, subtraction


def test_add() -> float:
    for x, y in zip(range(100), range(100)):
        assert addition(x, y) == x + y


def test_sub() -> float:
    for x, y in zip(range(100), range(100)):
        assert subtraction(x, y) == x - y


def test_multi() -> float:
    for x, y in zip(range(100), range(100)):
        assert multiplication(x, y) == x * y


def test_divi() -> float:
    for x, y in zip(range(100), range(1, 100)):
        assert division(x, y) == x / y


def test_divi_0_error() -> None:
    for x in range(100):
        y = 0
        with pytest.raises(ValueError, match="Cannot divide by 0"):
            division(x, y)


def test_slow_divi() -> float:
    for x, y in zip(range(100), range(1, 100)):
        assert slow_division(x, y) == x / y

def test_slow_divi_0_error() -> None:
    for x in range(100):
        y = 0
        with pytest.raises(ValueError, match="Cannot divide by 0"):
            slow_division(x, y)

def test_benchmark_slow_division(benchmark: None)-> None:
    benchmark(slow_division,2,1)
    
def test_benchmark_division(benchmark: None)-> None:
    benchmark(division,2,1)