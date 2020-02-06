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

def start_game():

    #Display initial board
    display_board()
    while game_going:
        handle_turn(current_player)
        check_game_over()

        change_player()

#Game Over
if winner == "X" or winner == "O":
    print(winner , "won.")


def handle_turn(player):
    position = input("Choose a position between 1 and 9: ")
    position = int(position) - 1
    board[position] = "X"
    display_board()

def check_game_over():
    check_win()
    check_tie()


def check_win():
    #Check rows
    #check columns
    #check diagonals
    return


def check_tie():

    return

def change_player():
    return
start_game()