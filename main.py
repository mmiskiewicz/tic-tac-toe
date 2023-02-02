import os

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
player1_turn = True
ascii_art = """\
___________.__               ___________                     ___________            
\__    ___/|__| ____         \__    ___/____    ____         \__    ___/___   ____  
  |    |   |  |/ ___\   ______ |    |  \__  \ _/ ___\   ______ |    | /  _ \_/ __ \ 
  |    |   |  \  \___  /_____/ |    |   / __  \  \___  /_____/ |    |(  <_> )  ___/ 
  |____|   |__|\___  >         |____|  (____  /\___  >         |____| \____/ \___  >
                   \/                       \/     \/                            \/ 
"""
wants_to_play = True


def print_board():
    """Prints out the tic-tac-toe board."""
    for row in range(3):
        for col in range(3):
            if col < 2:
                print(f"{board[row][col]} | ", end="")
            else:
                print(f"{board[row][col]} | ")
        if row < 2:
            print("-----------")


def check_coordinates(coordinates):
    """Checks if user's coordinates are correct."""
    row = int(coordinates[0])
    col = int(coordinates[2])
    if len(coordinates) != 3 or coordinates[1] != " ":
        print("Please try again and provide correct coordinates in format 'row col' (ex. 1 3).")
        ask_coordinates(player1_turn)
    elif 0 < row < 4 and 0 < col < 4:
        if "x" in board[row-1][col-1] or "o" in board[row-1][col-1]:
            print(f"Sorry, '{board[row-1][col-1].strip(' ')}' already exists in that spot.")
            ask_coordinates(player1_turn)
        else:
            print_coordinates(coordinates, player1_turn)


def ask_coordinates(player1_turn):
    """Asks the user for coordinates."""
    if player1_turn:
        coordinates = input("Player's 1 turn. Please provide 'X' coordinates in the following format 'row col': ")
    else:
        coordinates = input("Player's 2 turn. Please provide 'O' coordinates in the following format 'row col': ")
    try:
        check_coordinates(coordinates)
    except (IndexError, ValueError):
        print("Please try again and provide correct coordinates in format 'row col' (ex. 1 3).")
        ask_coordinates(player1_turn)


def print_coordinates(coordinates, player1_turn):
    """Adds the symbol into the board."""
    if player1_turn:
        board[int(coordinates[0])-1][int(coordinates[2])-1] = "x"
    else:
        board[int(coordinates[0])-1][int(coordinates[2])-1] = "o"


def game_over():
    """Checks if it's game over or not."""
    if " " not in board[0][:] and " " not in board[1][:] and " " not in board[2][:]:
        print(ascii_art)
        print_board()
        print("Draw!")
        return True
    elif board[0][0] == board[1][1] == board[2][2] != " " or board[2][0] == board[1][1] == board[0][2] != " ":
        print(ascii_art)
        print_board()
        if board[1][1] == "x":
            print("Player 1 win!")
        else:
            print("Player 2 win!")
        return True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
            print(ascii_art)
            print_board()
            if board[i][0] == "x" or board[0][i] == "x":
                print("Player 1 win!")
            else:
                print("Player 2 win!")
            return True
    return False


while wants_to_play:
    if not game_over():
        print(ascii_art)
        print_board()
        ask_coordinates(player1_turn)
        player1_turn = not player1_turn
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        wants_to_play = input("Would you like to continue playing? Type 'y' for yes or 'n' for no: ")
        while wants_to_play != 'n' and wants_to_play != 'y':
            print("Sorry, I didn't get that.")
            wants_to_play = input("Would you like to continue playing? Type 'y' for yes or 'n' for no: ").lower()
        if wants_to_play == "y":
            wants_to_play = True
            board = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "],
            ]
            player1_turn = True
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            wants_to_play = False
