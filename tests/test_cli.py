from io import StringIO
from calcapp import cli

def run_session(lines):
    inp = StringIO("\n".join(lines) + ("\n" if lines and not lines[-1].endswith("\n") else ""))
    out = StringIO()
    cli.run_rePL(inp, out)
    return out.getvalue()

def test_happy_path_add():
    out = run_session(["+", "2 3", "quit"])
    assert "Result: 5.0" in out
    assert "Welcome to pycalc!" in out

def test_invalid_op_then_quit():
    out = run_session(["foo", "quit"])
    assert "Unknown operation" in out

def test_invalid_numbers_then_quit():
    out = run_session(["+", "a b", "quit"])
    assert "Both values must be numbers." in out

def test_divide_by_zero_then_quit():
    out = run_session(["/", "1 0", "quit"])
    assert "Cannot divide by zero" in out

def test_help_message():
    out = run_session(["help", "quit"])
    assert "Operations:" in out
    assert "Goodbye!" in out
