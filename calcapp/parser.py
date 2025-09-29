from typing import Callable, Tuple
from . import operations

class InputError(ValueError):
    """User-facing input/validation error."""


_OPS = {
    "+": operations.add,
    "add": operations.add,
    "plus": operations.add,
    "-": operations.subtract,
    "sub": operations.subtract,
    "subtract": operations.subtract,
    "*": operations.multiply,
    "x": operations.multiply,
    "mul": operations.multiply,
    "multiply": operations.multiply,
    "/": operations.divide,
    "div": operations.divide,
    "divide": operations.divide,
}


def parse_operation(raw: str) -> Callable[[float, float], float]:
    key = (raw or "").strip().lower()
    func = _OPS.get(key)
    if not func:
        raise InputError(f"Unknown operation: {raw!r}. Use one of +, -, *, / or add/subtract/multiply/divide.")
    return func


def parse_two_numbers(raw: str) -> Tuple[float, float]:
    """Parse two numbers separated by space or comma. Raises InputError on invalid input."""
    if raw is None:
        raise InputError("Expected two numbers, got nothing.")
    cleaned = raw.replace(",", " ").strip()
    parts = [p for p in cleaned.split() if p]
    if len(parts) != 2:
        raise InputError("Please enter exactly two numbers (e.g., '2 3' or '2,3').")
    try:
        a, b = float(parts[0]), float(parts[1])
    except ValueError as exc:
        raise InputError("Both values must be numbers.") from exc
    return a, b
