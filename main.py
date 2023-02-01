import os

BOARD = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
PLAYER1_TURN = True
ASCII_ART = """\
___________.__               ___________                     ___________            
\__    ___/|__| ____         \__    ___/____    ____         \__    ___/___   ____  
  |    |   |  |/ ___\   ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ 
  |    |   |  \  \___  /_____/ |    |   / __  \  \___  /_____/ |    |(  <_> )  ___/ 
  |____|   |__|\___  >         |____|  (____  /\___  >         |____| \____/ \___  >
                   \/                       \/     \/                            \/ 
"""


def print_board():
    """Prints out the tic-tac-toe board."""
    for row in range(3):
        for col in range(3):
            if col < 2:
                print(f"{BOARD[row][col]} | ", end="")
            else:
                print(f"{BOARD[row][col]} | ")
        if row < 2:
            print("-----------")


def check_coordinates(coordinates):
    """Checks if user's coordinates are correct."""
    row = int(coordinates[0])
    col = int(coordinates[2])
    if len(coordinates) != 3 or coordinates[1] != " ":
        print("Please try again and provide correct coordinates in format 'row col' (ex. 1 3).")
        ask_coordinates(PLAYER1_TURN)
    elif 0 < row < 4 and 0 < col < 4:
        if "x" in BOARD[row-1][col-1] or "o" in BOARD[row-1][col-1]:
            print(f"Sorry, '{BOARD[row-1][col-1].strip(' ')}' already exists in that spot.")
            ask_coordinates(PLAYER1_TURN)
        else:
            print_coordinates(coordinates, PLAYER1_TURN)


def ask_coordinates(PLAYER1_TURN):
    """Asks the user for coordinates."""
    if PLAYER1_TURN:
        coordinates = input("Player's 1 turn. Please provide 'X' coordinates in the following format 'row col': ")
    else:
        coordinates = input("Player's 2 turn. Please provide 'O' coordinates in the following format 'row col': ")
    try:
        check_coordinates(coordinates)
        # print_coordinates(coordinates, PLAYER1_TURN)
    except (IndexError, ValueError):
        print("Please try again and provide correct coordinates in format 'row col' (ex. 1 3).")
        ask_coordinates(PLAYER1_TURN)


def print_coordinates(coordinates, PLAYER1_TURN):
    """Adds the symbol into the board."""
    if PLAYER1_TURN:
        BOARD[int(coordinates[0])-1][int(coordinates[2])-1] = "x"
    else:
        BOARD[int(coordinates[0])-1][int(coordinates[2])-1] = "o"


def game_over():
    """Checks if it's game over or not."""
    if " " not in BOARD[0][:] and " " not in BOARD[1][:] and " " not in BOARD[2][:]:
        print(ASCII_ART)
        print_board()
        print("Draw!")
        return True
    elif BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != " " or BOARD[2][0] == BOARD[1][1] == BOARD[0][2] != " ":
        print(ASCII_ART)
        print_board()
        if BOARD[1][1] == "x":
            print("Player 1 win!")
        else:
            print("Player 2 win!")
        return True
    for i in range(3):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] != " " or BOARD[0][i] == BOARD[1][i] == BOARD[2][i] != " ":
            print(ASCII_ART)
            print_board()
            if BOARD[i][0] == "x" or BOARD[0][i] == "x":
                print("Player 1 win!")
            else:
                print("Player 2 win!")
            return True
    return False


while not game_over():
    print(ASCII_ART)
    print_board()
    ask_coordinates(PLAYER1_TURN)
    PLAYER1_TURN = not PLAYER1_TURN
    os.system('cls' if os.name == 'nt' else 'clear')
