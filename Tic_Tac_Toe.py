from Tic_Tac_Toe_Func_Core import *
#===========GLOBAL VARIABLES===========


#GameBoard
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#Game still going
game_going = True

#Winner or Tie
winner = None

#Current Players
current_player = "X"

#Display board
def display_board():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")


#start the game Tic Tac Toe
def start_game():

    #Display initial board
    display_board()

    #While the game is still going
    while game_going:
        #Handle the single turn of the current player
        handle_turn(current_player)
        #Chech if the game is over
        check_game_over()
        #Change the current player
        change_player()

    #Game Over
    if winner == "X" or winner == "O":
        print(winner , "won.")
    elif winner == None:
        print("Tie.")

#Handle single player turn.
def handle_turn(player):
    position = input("Choose a position between 1 and 9: ")
    position = int(position) - 1
    board[position] = player
    display_board()

def check_game_over():
    check_win()
    check_tie()


def check_win():
    #Set up global variables
    global winner
    #Check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_column()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return
def check_rows():
    #Set up global variables
    global game_going
    #Check if all row have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column():
    #Set up global variables
    global game_going
    #Check if all column have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #Set up global variables
    global game_going
    #Check if all diagonals have the same value
    diagonal_1 = board[6] == board[4] == board[2] != "-"
    diagonal_2 = board[0] == board[4] == board[8] != "-"
    if diagonal_1 or diagonal_2:
        game_going = False
    if diagonal_1:
        return board[6]
    elif diagonal_2:
        return board[0]

    return


def check_tie():
    global game_going
    if "-" not in board:
        game_going = False
        return

def change_player():
    #Set up global variable.
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return



start_game()