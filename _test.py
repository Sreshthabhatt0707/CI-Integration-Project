import pytest


def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def fifth_power(x):
    return x ** 5


def test_square():
    assert square(2) == 4 , "Expected square of 2 to be 4"
    assert square(-3) == 9, "Expected square of -3 to be 9"
    assert square(0) == 0, "Expected square of 0 to be 0"

def test_cube():
    assert cube(2) == 8, "Expected cube of 2 to be 8"
    assert cube(-3) == -27, "Expected cube of -3 to be -27"
    assert cube(0) == 0, "Expected cube of 0 to be 0"


def test_fifth_power():
    assert fifth_power(2) == 32, "Expected fifth power of 2 to be 32"
    assert fifth_power(-3) == -243, "Expected fifth power of -3 to be -243"
    assert fifth_power(0) == 0, "Expected fifth power of 0 to be 0"