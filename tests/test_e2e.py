# Add the src directory to the Python path so imports always work,
# no matter where you run pytest from. This is the easiest way for beginners!
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import builtins
import main

def test_x_wins(monkeypatch, capsys):
    # Simulate a game where X wins in the top row
    moves = iter([
        "0,0",  # X
        "1,0",  # O
        "0,1",  # X
        "1,1",  # O
        "0,2"   # X wins
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(moves))
    main.main()
    out = capsys.readouterr().out
    assert "Player X wins!" in out

def test_draw(monkeypatch, capsys):
    # Simulate a game that ends in a draw
    moves = iter([
        "0,0", "0,1", "0,2",
        "1,1", "1,0", "1,2",
        "2,1", "2,0", "2,2"
    ])
    monkeypatch.setattr(__import__('builtins'), "input", lambda _: next(moves))
    main.main()
    out = capsys.readouterr().out
    assert "It's a draw!" in out