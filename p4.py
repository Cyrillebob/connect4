from termcolor import * 
from random import *
def display(board):
    """
    return the thing to print
    Parameters
    ----------
    board: the board of the game (list of list)
    Returns
    -------
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
               stprint += colored('        ', 'green', 'on_green')
           elif pawn == 1:
               stprint += colored( '        ', 'red', 'on_purple')
           else:
               stprint += colored ('        ', 'blue' ,'on_green')
        stprint += '\n'
        stprint += 2*stprint
        sprint += stprint
        stprint = ''
    return sprint     
board =[[0 for i in range(7)] for i in range (6)]
print(display(board))