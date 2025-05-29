def check_win(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def is_valid_move(board, row, col):
    # already know row and col are integers from input_handler
    if not (0 <= row < 3 and 0 <= col < 3):
        raise ValueError(">> Row and column must be between 0 and 2.")
    if board[row][col] != " ":
        raise ValueError(f">> Cell ({row},{col}) is already taken. Please choose another spot.")
    return True

def make_move(board, row, col, player):
    is_valid_move(board, row, col)
    board[row][col] = player

if __name__ == "__main__":
    # Test win detection
    win_board = [
        ["X", "X", "X"],
        ["O", " ", "O"],
        [" ", " ", " "]
    ]
    print("Win test (should be True):", check_win(win_board))

    # Test draw detection
    draw_board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    print("Draw test (should be True):", check_draw(draw_board))

    # Test invalid move (out of range)
    try:
        is_valid_move(draw_board, 3, 0)
    except ValueError as e:
        print("Out of range test:", e)

    # Test invalid move (cell taken)
    try:
        is_valid_move(draw_board, 0, 0)
    except ValueError as e:
        print("Cell taken test:", e)

    # Test valid move
    try:
        print("Valid move test (should be True):", is_valid_move(draw_board, 1, 1))
    except ValueError as e:
        print("Valid move test failed:", e)