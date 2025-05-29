from logic import check_win, check_draw, make_move, is_valid_move
from display import print_board, print_winner, print_draw
from input_handler import get_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    try:
        while True:
            print_board(board, in_game=True)
            row, col = get_move(current_player, board)
            try:
                make_move(board, row, col, current_player)
            except ValueError as e:
                print(e)
                continue

            if check_win(board):
                print_board(board, in_game=False)
                print_winner(current_player)
                break
            if check_draw(board):
                print_board(board, in_game=False)
                print_draw()
                break
            current_player = "O" if current_player == "X" else "X"
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!\n")

if __name__ == "__main__":
    main()