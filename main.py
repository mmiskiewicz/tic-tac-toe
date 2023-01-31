GAME_OVER = False
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" x", " ", " "],
]


def print_board():
    """Prints out the tic-tac-toe board."""
    for row in range(3):
        for col in range(3):
            if col < 2:
                print(" | ", end="")
            else:
                print(" | ")
        if row < 2:
            print("-----------")


def check_coords(coords):
    """Checks if user's coordinates are correct."""
    row = int(coords[0])
    col = int(coords[2])
    if 0 < row < 4 and 0 < col < 4:
        if "x" in board[row-1][col-1] or "o" in board[row-1][col-1]:
            print(f"Sorry, '{board[row-1][col-1].strip(' ')}' already exists in that spot.")
    else:
        print("Please try again and provide correct coordinates in format 'row col' (ex. 1 3).")


# coords = input("Player's 1 turn. Please provide X's coords in the following format 'row col': ")
# print_board()
# check_coords(coords)
# while not GAME_OVER:
#     pass
