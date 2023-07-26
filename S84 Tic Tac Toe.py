
game_on=True
current_player = "X"
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
positions=[1,2,3,4,5,6,7,8,9]
def game_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "\n" +
          board[3] + "|" + board[4] + "|" + board[5] + "\n" +
          board[6] + "|" + board[7] + "|" + board[8] + "\n")
def board_show(player):
    global game_on
    game_board()

    place= int(input(f"{player}'s turn: "))

    if place in positions:
        if board[place-1] == "X" or board[place-1] == "O":
            print("OOPs Position already filled, give another number")
            board_show(player)
        else:
            board[place-1]=player
    else:
        print("Wrong input")
        board_show(player)


    #check
def win_game():
    global game_on
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col1 = board[0] == board[3] == board[6] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"
    if row1 or row2 or row3 or col1 or col2 or col3 or dia1 or dia2:

        game_board()
        print(f"congo! player '{current_player}' you Won the  game")
        rematch()
        return True

def tie_game():
    global game_on
    if "-" not in board:
        print("Game Tie!")
        rematch()




def players_turn():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"



def check_game_status():
    if not win_game():
        tie_game()

def rematch():
    global game_on, board
    rematch= input("Rematch? (y/n)")
    if rematch.lower()=="y":
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        game_on=True
    else:
        game_on=False

while game_on:
    board_show(current_player)
    check_game_status()
    players_turn()





