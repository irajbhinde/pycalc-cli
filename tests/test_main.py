from io import StringIO
import sys
from calcapp import cli

def test_main_runs_and_quits(monkeypatch):
    monkeypatch.setattr(sys, "stdin", StringIO("quit\n"))
    buf = StringIO()
    monkeypatch.setattr(sys, "stdout", buf)
    cli.main()
    assert "Goodbye!" in buf.getvalue()
