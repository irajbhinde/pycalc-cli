from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Return a + b as float."""
    return float(a) + float(b)


def subtract(a: Number, b: Number) -> float:
    """Return a - b as float."""
    return float(a) - float(b)


def multiply(a: Number, b: Number) -> float:
    """Return a * b as float."""
    return float(a) * float(b)


def divide(a: Number, b: Number) -> float:
    """Return a / b as float. Raises ZeroDivisionError for b == 0."""
    b = float(b)
    if b == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return float(a) / b
