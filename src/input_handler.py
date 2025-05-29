from logic import is_valid_move

def get_move(player, board):
    while True:
        move = input(f"Player {player}, enter your move as 'row,col' (e.g., 1,2): ")
        try:
            row_str, col_str = move.strip().split(",")
            row, col = int(row_str), int(col_str)
        except ValueError:
            print(">> Invalid input format\nPlease enter two numbers separated by a comma, e.g.: 1,2")
            continue

        try:
            is_valid_move(board, row, col)
        except ValueError as e:
            print(e)
            continue

        return row, col

if __name__ == "__main__":
    # Demo: get a move from the user and validate it on an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    move = get_move("X", board)
    print(f"Received move: {move}")