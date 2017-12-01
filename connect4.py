from termcolor import *

def print_board(board):
    """
    print the thing to print
    Parameters
    ----------
    board: the board of the game (list of list)
    Print
    -----
    sprint: the sentence to print (str)
    """
    sprint = ''
    stprint = ''
    i = 0
    j=0
    for line in board:
        i+=1
        for pawn in line:
           j+=1
           if pawn == 0:
               stprint += colored('       ', 'green', 'on_green')
           elif pawn == 1:
               stprint += colored('       ', 'magenta', 'on_magenta')
           else:
               stprint += colored ('       ', 'blue' ,'on_blue')
        stprint += '\n'
        stprint += 2*stprint
        sprint += stprint
        stprint = ''
    s= ''
    for i in range(1,8):
        s += '   %d   '%i
    s+= '\n'
    sprint =  s + sprint
    print (sprint)

def play():
    """
    create a game"""
    player = 1
    board = create_board()
    while check_win(board) == 0:
        print_board(board)
        print ('Player %d, what column do you wish to play on? \n' % player)
        column = input ()
        try:
            column = int(column) - 1
            if column < 0 or column > 6:
                print('You fucking bastard don\'t try to cheat it\'s obvious that you can\'t place a pawn in this column, please die.\n')
            else:
                board, ok_move = place_pawn(player, column, board)
                if ok_move:
                    player = player % 2 + 1
                else:
                    print('You fucking bastard don\'t try to cheat it\'s obvious that you can\'t place a pawn in this column, please die.\n')
        except:
            print('NaN\n')
    print_board(board)        
    if check_win(board) == 1:
        print('PLAYER 1 WINS\n')
    elif check_win(board) == 2:
        print('PLAYER 2 WINS\n')
    elif check_win(board) == 3:
        print('DRAW\n')
    else:
        print('error\n')
                        
def create_board():
    """
    returns
    -------
    board: the empty board for the game"""
    
    board = [[0 for _ in range(7)] for _ in range (6)]
    return board
    
    
def check_win(board):
    """
    returns
    -------
    0 if the game isn't ended
    1 if the player one has won
    2 if the player two has won
    3 if draw"""
    
    # 1 : check lines
    
    for i in range (6):
        for j in range(4):
            pawn = board[i][j]
            if (pawn) > 0:
                if pawn == board[i][j+1] and pawn == board[i][j+2] and pawn == board[i][j+3]:
                    return pawn
                    
    # 2 : check columns
    
    for i in range (3):
        for j in range(7):
            pawn = board[i][j]
            if (pawn) > 0:
                if pawn == board[i+1][j] and pawn == board[i+2][j] and pawn == board[i+3][j]:
                    return pawn
    
    
    # 3 : check lower diags
    
    for i in range (3):
        for j in range(4):
            pawn = board[i][j]
            if (pawn) > 0:
                if pawn == board[i+1][j+1] and pawn == board[i+2][j+2] and pawn == board[i+3][j+3]:
                    return pawn
    
    # 4 : check upper diags
    
    for i in range (3,6):
        for j in range(4):
            pawn = board[i][j]
            if (pawn) > 0:
                if pawn == board[i-1][j+1] and pawn == board[i-2][j+2] and pawn == board[i-3][j+3]:
                    return pawn
                    
    # 5 : check draw
    
    for i in range (6):
        for j in range(7):
            if (board[i][j]) == 0:
                return 0
                    
    return 3
    
def place_pawn(player, column, board):
    """
    place a pawn for a player
    return
    ------
    - the changed board
    - 1 if a pawn was added, 0 otherwise"""
    for line in range(6):
        line = 5-line
        if board[line][column] == 0:
           board[line][column] = player
           return board, 1
    return board, 0
    