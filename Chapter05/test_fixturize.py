import pytest
from functions import *

@pytest.fixture()
def fixturized_value():
    return 1

def test_sum_with_fixture(fixturized_value):
    fixturized_value = sum(0,fixturized_value)
    assert fixturized_value == 1

def is_odd(n):
    return n % 2 != 0

def sum(a,b):
    return a + b

@pytest.mark.parametrize(
    'num',(1,3,5),
)
def test_odd_numbers(num):
    assert is_odd(num), f"{num} should be odd!"

@pytest.mark.parametrize(
    'nums', [
        (1,2,3),
        (4,5,6),
        (7,8,15),
        (1,11,12),
    ]
)
def test_sum_numbers(nums):
    a, b, c = nums
    assert sum(a,b) == c, f"{a} + {b} == {c} should be the case!"