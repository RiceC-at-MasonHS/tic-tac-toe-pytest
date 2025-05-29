# Add the src directory to the Python path so imports always work,
# no matter where you run pytest from. This is the easiest way for beginners!
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from logic import make_move, check_win, check_draw

def test_full_game_x_wins():
    board = [[" " for _ in range(3)] for _ in range(3)]
    moves = [
        (0, 0, "X"), (1, 0, "O"),
        (0, 1, "X"), (1, 1, "O"),
        (0, 2, "X")
    ]
    for row, col, player in moves:
        make_move(board, row, col, player)
    assert check_win(board)
    assert not check_draw(board)

def test_full_game_draw():
    board = [[" " for _ in range(3)] for _ in range(3)]
    moves = [
        (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
        (1, 1, "O"), (1, 0, "X"), (1, 2, "O"),
        (2, 0, "O"), (2, 2, "X"), (2, 1, "X")
    ]
    for row, col, player in moves:
        make_move(board, row, col, player)
    assert not check_win(board)
    assert check_draw(board)