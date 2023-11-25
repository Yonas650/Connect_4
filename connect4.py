import random
import os
NUM_ROWS =6
NUM_COLS =7
CHECKER_1 = 'X'
CHECKER_2 = 'O'
CHECKER_3='V'
CHECKER_4='H'
CHECKER_5='M'
NUM_PLAYERS = 2
board = []

for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
        row_list.append(' ')
    board.append(row_list)
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(board[row][col],end='')
    print()
#The above code creates a 2-D list

arr=[]     # this list accumulates letters and I use it later as a range to handle an error and access columns
for cols in range(NUM_COLS): 
    print('   ' + chr(cols+65), end='')
    arr.append(chr(cols+65))
print('\n +' + "---+" * NUM_COLS) #prints the top border of the box

for row in range(NUM_ROWS): #this nested for loop prints the rest of the board except the top border
    print(' |', end=' ')
    for col in range(NUM_COLS): 
        print(board[row][col] + ' | ', end='') 
    print("\n +"+"---+"*NUM_COLS)
first_turn = random.randint(0, NUM_PLAYERS - 1) #this random function chooses a radom player to start the game
if first_turn==0: #this if condition assign checkers and prints the current player
    CHECKER=CHECKER_1
    print('player1')
elif first_turn==1:
    CHECKER=CHECKER_2
    print('player2')
elif first_turn==2:
    CHECKER=CHECKER_3
    print('player3')
elif first_turn==3:
    CHECKER=CHECKER_4
    print('player4')
else:
    CHECKER=CHECKER_5
    print('player5')

no_4chekers=True
not_full=True
while not_full and no_4chekers:#the while loop for the whole game
    location=input('please enter the column you want to play:' )#accepts coordinate inputes from the user
    while len(location)==0 or not location[0] in arr or len(location)!=1: #checking for invalid user input
      print('error! you inserted an invalid input or index out of range! ')
      location=input('please enter the column:' )
    for row in range(NUM_ROWS-1, -1, -1):#places the checker in the right location
        if board[row][arr.index(location)]==' ':
            board[row][arr.index(location)] = CHECKER
            break

                
    os.system('clear') #clears the window after each excution
        
    for cols in range(NUM_COLS):   #this for loop prints the top border of the board and the letters
       print('   ' + chr(cols+65), end='')
    print("\n +" + "---+" * NUM_COLS)
    
    for row in range(NUM_ROWS): #this for loop prints the rest of the board including entries
       print(' |', end=' ')
       for col in range(NUM_COLS): 
         print(board[row][col] + ' | ', end='') 
       print("\n +"+"---+"*NUM_COLS)
    not_full=False
    for row in range(NUM_ROWS-1, -1, -1):#checks if the board is full or not
        for col in range(NUM_COLS-1,-1,-1):
            if  board[row][col]==' ':
                not_full=True
    for row in range(NUM_ROWS-1, -1, -1):# checks for a win horizontally
        for col in range(NUM_COLS-1,-1,-1):
            if board[row][col]=='X' and board[row][col-1]=='X' and board[row][col-2]=='X' and board[row][col-3]=='X':
                no_4chekers=False
            elif board[row][col]=='O' and board[row][col-1]=='O' and board[row][col-2]=='O' and board[row][col-3]=='O':
                no_4chekers=False
            elif board[row][col]=='V' and board[row][col-1]=='V' and board[row][col-2]=='V' and board[row][col-3]=='V':
                no_4chekers=False
            elif board[row][col]=='H' and board[row][col-1]=='H' and board[row][col-2]=='H' and board[row][col-3]=='H':
                no_4chekers=False
            elif board[row][col]=='M' and board[row][col-1]=='M' and board[row][col-2]=='M' and board[row][col-3]=='M':
                no_4chekers=False
    for row in range(NUM_ROWS-1, -1, -1):#checks for a win vertically
        if board[row][arr.index(location)]=='X' and board[row-1][arr.index(location)]=='X' and board[row-2][arr.index(location)]=='X' and board[row-3][arr.index(location)]=='X':
            no_4chekers=False
        elif board[row][arr.index(location)]=='O' and board[row-1][arr.index(location)]=='O' and board[row-2][arr.index(location)]=='O' and board[row-3][arr.index(location)]=='O':
            no_4chekers=False
        elif board[row][arr.index(location)]=='V' and board[row-1][arr.index(location)]=='V' and board[row-2][arr.index(location)]=='V' and board[row-3][arr.index(location)]=='V':
            no_4chekers=False
        elif board[row][arr.index(location)]=='H' and board[row-1][arr.index(location)]=='H' and board[row-2][arr.index(location)]=='H' and board[row-3][arr.index(location)]=='H':
            no_4chekers=False
        elif board[row][arr.index(location)]=='M' and board[row-1][arr.index(location)]=='M' and board[row-2][arr.index(location)]=='M' and board[row-3][arr.index(location)]=='M':
            no_4chekers=False
    try:#checks for a win diagonally
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if board[row][col]=='X' and board[row-1][col-1]=='X' and board[row-2][col-2]=='X' and board[row-3][col-3]=='X':
                     no_4chekers=False
                elif board[row][col]=='X' and board[row+1][col-1]=='X' and board[row+2][col-2]=='X' and board[row+3][col-3]=='X':
                     no_4chekers=False
                elif board[row][col]=='X' and board[row+1][col+1]=='X' and board[row+2][col+2]=='X' and board[row+3][col+3]=='X':
                     no_4chekers=False
                elif board[row][col]=='X' and board[row-1][col+1]=='X' and board[row-2][col+2]=='X' and board[row-3][col+3]=='X':
                     no_4chekers=False
                
                elif board[row][col]=='O' and board[row-1][col-1]=='O' and board[row-2][col-2]=='O' and board[row-3][col-3]=='O':
                     no_4chekers=False
                elif board[row][col]=='O' and board[row+1][col-1]=='O' and board[row+2][col-2]=='O' and board[row+3][col-3]=='O':
                     no_4chekers=False
                elif board[row][col]=='O' and board[row+1][col+1]=='O' and board[row+2][col+2]=='O' and board[row+3][col+3]=='O':
                     no_4chekers=False
                elif board[row][col]=='O' and board[row-1][col+1]=='O' and board[row-2][col+2]=='O' and board[row-3][col+3]=='O':
                     no_4chekers=False
                
                elif board[row][col]=='V' and board[row-1][col-1]=='V' and board[row-2][col-2]=='V' and board[row-3][col-3]=='V':
                     no_4chekers=False
                elif board[row][col]=='V' and board[row+1][col-1]=='V' and board[row+2][col-2]=='V' and board[row+3][col-3]=='V':
                     no_4chekers=False
                elif board[row][col]=='V' and board[row+1][col+1]=='V' and board[row+2][col+2]=='V' and board[row+3][col+3]=='V':
                     no_4chekers=False
                elif board[row][col]=='V' and board[row-1][col+1]=='V' and board[row-2][col+2]=='V' and board[row-3][col+3]=='V':
                     no_4chekers=False
                
                elif board[row][col]=='H' and board[row-1][col-1]=='H' and board[row-2][col-2]=='H' and board[row-3][col-3]=='H':
                     no_4chekers=False
                elif board[row][col]=='H' and board[row+1][col-1]=='H' and board[row+2][col-2]=='H' and board[row+3][col-3]=='H':
                     no_4chekers=False
                elif board[row][col]=='H' and board[row+1][col+1]=='H' and board[row+2][col+2]=='H' and board[row+3][col+3]=='H':
                     no_4chekers=False
                elif board[row][col]=='H' and board[row-1][col+1]=='H' and board[row-2][col+2]=='H' and board[row-3][col+3]=='H':
                     no_4chekers=False
                
                elif board[row][col]=='M' and board[row-1][col-1]=='M' and board[row-2][col-2]=='M' and board[row-3][col-3]=='M':
                     no_4chekers=False
                elif board[row][col]=='M' and board[row+1][col-1]=='M' and board[row+2][col-2]=='M' and board[row+3][col-3]=='M':
                     no_4chekers=False
                elif board[row][col]=='M' and board[row+1][col+1]=='M' and board[row+2][col+2]=='M' and board[row+3][col+3]=='M':
                     no_4chekers=False
                elif board[row][col]=='M' and board[row-1][col+1]=='M' and board[row-2][col+2]=='M' and board[row-3][col+3]=='M':
                     no_4chekers=False
    except IndexError:
        print()

    if CHECKER==CHECKER_1:#saves the winner
        winner='player1'
    elif CHECKER==CHECKER_2:
        winner='player2'
    elif CHECKER==CHECKER_3:
        winner='player3'
    elif CHECKER==CHECKER_4:
        winner='player4'
    else:
        winner='player5'
    
    if first_turn==NUM_PLAYERS-1:#alternates the turn
        first_turn=-1
    first_turn=first_turn+1
    if first_turn==0: #this if condition assign checkers and prints the current player
        CHECKER=CHECKER_1
        print('player1')
    elif first_turn==1:
        CHECKER=CHECKER_2
        print('player2')
    elif first_turn==2:
        CHECKER=CHECKER_3
        print('player3')
    elif first_turn==3:
        CHECKER=CHECKER_4
        print('player4')
    else:
        CHECKER=CHECKER_5
        print('player5')
print('game over')
if no_4chekers==False and not_full==True:#prints the winner
    print('The winner is',winner+'!')

else:#prints a draw
    print('The game is a draw')