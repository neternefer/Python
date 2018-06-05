#Kółko i krzyżyk 1.0

#Stałe
BOXES = 9
X = "X"
O = "0"
TIE = "tie"
EMPTY = " "

#Powitanie
def display_info():
    print("""Witaj w grze. Znasz reguły.
             Oto plansza:

             0 | 1 | 2
             ---------
             3 | 4 | 5
             ---------
             6 | 7 | 8

             Powodzenia!
             """)

def ask(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high, step=1):
    number = None
    while number not in range(low, high):
        number = int(input(question))
    return number

def new_board():
    board = []
    for box in range(BOXES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t","---------")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t","---------")
    print("\t",board[6],"|",board[7],"|",board[8])

def change_turn(turn):
    if turn == X:
        return 0
    else:
        return X

def pieces():
    go_first = ask("Czy chcesz rozpocząć grę? ")
    if go_first == "t":
        human = X
        computer = 0
    else:
        computer = X
        human = 0
    return computer, human

def legit_moves(board):
    leg = []
    for box in range(BOXES):
        if board[box] == EMPTY:
            leg.append(box)
    return leg

def player_move(board, human):
    good = legit_moves(board)
    move = None
    while move not in good:
        move = ask_number("Podaj numer od 0 do 8: ", 0, 9)
        if move not in good:
            print("To miejsce jest już zajęte!")
    print("Doskonale!")
    return move


def comp_move(board,computer, human):
    good = legit_moves(board)
    win = winner(board)
    best = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    board = board[:]
    for move in good:
        board[move] = computer
        if win == computer:
            return move
        board[move] = EMPTY
    for move in good:
        board[move] = human
        if win == human:
            return move
        board[move] = EMPTY
    for move in best:
        if move in good:
           board[move] = computer
           return move
    


def winner(board):
    WAYS = [(0, 1, 2), (3, 4, 5),
            (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    for move in WAYS:
        if board[move[0]] == board[move[1]] == board[move[2]] != EMPTY:
            winner = board[move[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None




def congrats(the_winner, human, computer):
    if the_winner != TIE:
        print("Zwyciężył",the_winner)
    else:
        print("Remis!")
    


def main():
    display_info()
    board = new_board()
    display_board(board)
    computer, human = pieces()
    turn = X
    while not winner(board):
        if turn == human:
            move = player_move(board, human)
            board[move] = human
        else:
            move = comp_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = change_turn(turn)
    the_winner = winner(board)
    congrats(the_winner, human, computer)
    
        
main()
input("Press Enter to exit")
