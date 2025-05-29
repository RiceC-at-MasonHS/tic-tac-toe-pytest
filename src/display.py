import os

def clear_terminal():
    if os.system("clear") != 0:
        os.system("cls")

# ASCII art for X and O (3x3), with horizontal padding for a square look
X_ART = [
    "   \\ /   ",
    "    X    ",
    "   / \\   "
]
O_ART = [
    "   /-\\   ",
    "  |   |  ",
    "   \\-/   "
]
EMPTY_ART = [
    "         ",
    "         ",
    "         "
]

def print_board(board, in_game=True):
    clear_terminal()
    print("Tic-Tac-Toe")
    if in_game:
        print("No one has won yet, keep playing!")
    print()

    # Print column titles (0, 1, 2) above the board
    print("         0           1           2\n")

    # Build each row of the board in ASCII art with horizontal padding
    for row_idx, row in enumerate(board):
        
        # The ASCII art for each row is 3x3, so we need to print each line of the art
        for art_line in range(3):
            
            # start with a blank line, to draw the ASCII art
            line = ""
            
            # add row number, if on ASCII art line 1 of [0,1,2]
            if art_line == 1:  # Center row number vertically in the cell
                line += f" {row_idx}   "
            else:
                line += "     "
            
            # Add the ASCII art for each cell in the row
            for col_idx, cell in enumerate(row):
                if cell == "X":
                    art = X_ART
                elif cell == "O":
                    art = O_ART
                else:
                    art = EMPTY_ART

                # Add the corresponding line of ASCII art for the cell
                line += art[art_line]
                
                # Add vertical separator, if not the last column
                if col_idx < 2:
                    line += " | "

            # Print the constructed line for the current row
            print(line)

        # Print horizontal separator after each ASCII row (except the last)
        if row_idx < 2:
            print("     " + "-" * 33)
    print()

def print_winner(player):
    print(f"Player {player} wins!")

def print_draw():
    print("It's a draw!")

def print_invalid_move():
    print("Cell already taken, try again.")

if __name__ == "__main__":
    # Show a sample board with all display features
    test_board = [
        ["X", "O", "X"],
        [" ", "X", "O"],
        ["O", " ", "X"]
    ]
    print_board(test_board)
    print_winner("X")
    print_draw()
    print_invalid_move()