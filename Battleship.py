#!usr/bin/python
from random import randint  # makes a random integer between specified objects under def

NO_USER_GUESS = 10 # variable guess set
# initialising board
board = []

for x in range(5):          # 2D version of board
    board.append(["O"] * 5)

def print_board(board):
    print("###############")
    print("Battleships!")
    print("###############")
    for row in board:
        print ("  ".join(row))   # space between circles

#starting game and printing board
print("Take a guess between 0 and 4 on a row or column")
print("You have " + str(NO_USER_GUESS) +" turns to complete the game -\n")
print ("=" * 50 +"\n")          #makes lines between text and battleships
print_board(board)

#defining where the ship is
def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)
turn= 0            # makes variables to handle later

# asking user to guess
for attempt in range(NO_USER_GUESS):
    print("\n")
    guess_row = int(input("Guess Row \n"))
    guess_col = int(input("Guess Col \n"))

    # if user is correct
    if guess_row ==ship_row and guess_col == ship_col:
        board[guess_row][guess_col] == "*"  # star is placed in board where ship was hit
        print(" YOU SUNK MY BATTLESHIP!\n"
"                                      /    _,'|             \n"
"                                     /_ _,'   |     \n"
"                                    $$;'     _;     \n"
"                    ,-'-._    ,-'. ,-'    _.'\n"
"                    \     `-,'  ,-'    _,'\n"
"   _od8PP8booo   ,....       ;,'    ,,'  _____ \n"
" d8P''         ,'     \   _,'    ,-' ,oo8P""Y8.\n"
" `'             `-.    i,'    ,-',odPP''      8b\n"
"                   `-,'    ,-',o8P'          ,8P\n"
"                .',-'   ,-',o8P'             d8 \n"
"             .'.-'  _,-',o8P'               ,8P \n"
"           ',-'  _,' _o8P'                  dP \n"
"8bo,     _,'  _,'  ,dP'                    d8\n"
"  Y8'    \ ,,'  ,o8P'                    _op'                     _,d8P \n"
"  dP      '  ,o8P'                     ,o8'                   ,oo8P"'\n'
"  Yb     _oo8P'                      ,dP'                 ,odPP''\n"
"   Ybooo8P''                       ,dP'              _,odPP'\n"
"     ''                           o8'            _oo8P"'\n'
"                                ,8P         _,odPP''\n"
"                               d8'    __,odPP"'\n'
"                               Y8oooo8PP"'")\n')


        print("YOU WIN!!!")
        break
    else:
        # if guess is out of the board
        if(guess_row<0 or guess_row>4) or (guess_col<0 or guess_col>4):
            print("Your are out of bounds \n")

        # if guess already been made
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that already \n")

        # if guess is wrong, mark the point with an X and start again
        else:
            print("Haha!! You missed my battleship! \n")
            board[guess_row][guess_col]= "X"
            print_board(board)

# if user made 10 tries already, game over
if turn >= NO_USER_GUESS:
    print("GAME OVER")
