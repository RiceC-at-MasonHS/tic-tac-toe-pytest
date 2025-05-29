# Add the src directory to the Python path so imports always work,
# no matter where you run pytest from. This is the easiest way for beginners!
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from logic import check_win, check_draw, is_valid_move, make_move

def test_check_win_row():
    board = [
        ["X", "X", "X"],
        ["O", " ", "O"],
        [" ", " ", " "]
    ]
    assert check_win(board)

def test_check_win_col():
    board = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["O", " ", "X"]
    ]
    assert check_win(board)

def test_check_win_diag():
    board = [
        ["X", "O", "O"],
        [" ", "X", " "],
        ["O", " ", "X"]
    ]
    assert check_win(board)

def test_check_draw():
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    assert check_draw(board)

def test_is_valid_move_valid():
    board = [
        ["X", "O", "X"],
        ["X", " ", "O"],
        ["O", "X", "X"]
    ]
    assert is_valid_move(board, 1, 1)

def test_is_valid_move_out_of_range():
    board = [[" "]*3 for _ in range(3)]
    with pytest.raises(ValueError):
        is_valid_move(board, 3, 0)

def test_is_valid_move_taken():
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    with pytest.raises(ValueError):
        is_valid_move(board, 0, 0)

def test_make_move():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    make_move(board, 1, 1, "X")
    assert board[1][1] == "X"