from __future__ import annotations
import sys
from io import TextIOBase, StringIO
from typing import Optional, TextIO, Callable

from .parser import parse_operation, parse_two_numbers, InputError

HELP_TEXT = (
    "Operations: +, -, *, / (or add/subtract/multiply/divide)\n"
    "Type 'help' to see this message again. Type 'quit' or 'exit' to leave."
)


def run_rePL(in_stream: Optional[TextIO] = None, out_stream: Optional[TextIO] = None) -> None:
    """Run the interactive REPL. Streams are injectable for testing."""
    inp = in_stream or sys.stdin
    out = out_stream or sys.stdout

    print("Welcome to pycalc! A simple calculator.", file=out)
    print(HELP_TEXT, file=out)

    while True:
        print("Enter operation (+, -, *, /), or 'help'/'quit': ", end="", file=out)
        op_raw = inp.readline()
        if not op_raw:  # EOF
            print("\nGoodbye!", file=out)
            break

        op_key = op_raw.strip().lower()
        if op_key in {"quit", "q", "exit"}:
            print("Goodbye!", file=out)
            break
        if op_key in {"help", "h", "?"}:
            print(HELP_TEXT, file=out)
            continue

        try:
            op_func = parse_operation(op_key)
        except InputError as e:
            print(f"Error: {e}", file=out)
            continue

        print("Enter two numbers (e.g. 2 3 or 2,3): ", end="", file=out)
        nums_raw = inp.readline()
        try:
            a, b = parse_two_numbers(nums_raw)
        except InputError as e:
            print(f"Error: {e}", file=out)
            continue

        try:
            result = op_func(a, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}", file=out)
            continue

        print(f"Result: {result}", file=out)


def main() -> None:
    run_rePL()


if __name__ == "__main__":
    main()
