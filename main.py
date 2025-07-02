
#game board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

#if game is still on
game_on = True

winner = None
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2]) 
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8]) 

def play_game():
    global game_on
    display_board()

    while game_on:
        handle_turn(current_player)
        check_gameover()
        flip_player()

    #game ended
    if winner != None:
        print(winner + " won!")
    else:
        print("Tie")


def handle_turn(player):
    valid = False
    while not valid:
        position = input(f"{player}'s turn. Choose a position (1-9): ")
        if position not in map(str, range(1, 10)):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        position = int(position) - 1

        if board[position] != "-":
            print("Position already taken. Try again.")
            continue

        valid = True

    board[position] = player
    display_board()

def check_gameover():
    check_winner()
    check_istie()

def check_winner():
    global winner 

    #check row
    row = check_row()
    #check col
    col = check_col()
    #check diagonal
    diag = check_diag()

    if row or col or diag:
        winner = current_player
    return

def check_row():
    global game_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-" 
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_on = False
    if row_1:
        return board[0]
    elif  row_2:
        return board[3]
    elif  row_3:
        return board[6]
    return

def check_col():
    global game_on
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-" 
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_on = False
    if col_1:
        return board[0]
    elif  col_2:
        return board[1]
    elif  col_3:
        return board[2]
    return

def check_diag():
    global game_on
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-" 

    if diag_1 or diag_2:
        game_on = False
    if diag_1:
        return board[0]
    elif  diag_2:
        return board[2]

    return

def check_istie():
    global game_on
    if "-" not in board and winner == None:
        game_on = False
        return True
    return False



def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


play_game()