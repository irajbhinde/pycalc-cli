import sys, runpy
from io import StringIO

def test_module_entrypoint_guard(monkeypatch):
    # Provide input so the REPL can exit cleanly
    monkeypatch.setattr(sys, "stdin", StringIO("quit\n"))
    out = StringIO()
    monkeypatch.setattr(sys, "stdout", out)

    # This runs calcapp/cli.py as if "python -m calcapp.cli" (triggers the __main__ guard)
    runpy.run_module("calcapp.cli", run_name="__main__")

    assert "Goodbye!" in out.getvalue()
