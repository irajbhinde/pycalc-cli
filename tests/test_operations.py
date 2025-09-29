import pytest
from calcapp import operations

import math

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (1, 2, 3.0),
        (-1, 2.5, 1.5),
        (1.2, 3.4, 4.6),
    ],
)
def test_add(a, b, expected):
    assert operations.add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (2, 1, 1.0),
        (-1, 2.5, -3.5),
        (3.4, 1.2, 2.2),
    ],
)
def test_subtract(a, b, expected):
    assert operations.subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0.0),
        (2, 3, 6.0),
        (-1, 2.5, -2.5),
        (1.5, 2, 3.0),
    ],
)
def test_multiply(a, b, expected):
    assert operations.multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 1.0),
        (3, 2, 1.5),
        (-4, 2, -2.0),
        (1.5, 0.5, 3.0),
    ],
)
def test_divide(a, b, expected):
    assert operations.divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.divide(1, 0)
