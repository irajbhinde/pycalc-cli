import pytest
from calcapp import parser
from calcapp.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("token,func", [
    ("+", add), ("add", add), ("plus", add),
    ("-", subtract), ("sub", subtract), ("subtract", subtract),
    ("*", multiply), ("x", multiply), ("mul", multiply), ("multiply", multiply),
    ("/", divide), ("div", divide), ("divide", divide),
])
def test_parse_operation_success(token, func):
    assert parser.parse_operation(token) is func


@pytest.mark.parametrize("bad", ["", "  ", "unknown", "power", "%"])
def test_parse_operation_error(bad):
    with pytest.raises(parser.InputError):
        parser.parse_operation(bad)


@pytest.mark.parametrize("raw,a,b", [
    ("2 3", 2.0, 3.0),
    ("2,3", 2.0, 3.0),
    ("  -1.5 ,  2.25 ", -1.5, 2.25),
])
def test_parse_two_numbers_success(raw, a, b):
    assert parser.parse_two_numbers(raw) == (a, b)


@pytest.mark.parametrize("raw", [None, "", " ", "1", "1 2 3", "a b", "1,"])
def test_parse_two_numbers_error(raw):
    with pytest.raises(parser.InputError):
        parser.parse_two_numbers(raw)
