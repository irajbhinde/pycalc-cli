from io import StringIO
from calcapp import cli

def test_repl_eof_exits_gracefully():
    # Empty input simulates user pressing Ctrl+D / EOF immediately
    out = StringIO()
    cli.run_rePL(in_stream=StringIO(""), out_stream=out)
    text = out.getvalue()
    assert "Welcome to pycalc!" in text
    assert "Goodbye!" in text
