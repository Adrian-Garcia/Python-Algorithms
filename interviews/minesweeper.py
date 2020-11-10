"""
/**
*
* Implement Minesweeper Game. Example: http://minesweeperonline.com/. 
* 
* Design data structure to represent the game and create function(s).
*
* The board will contains only contains:
*   1) empty cell, representing with 'e'
*   2) mine cell, representing with 'm'
*   3) unvealed cell, representing with '#'
* 
* Example:
* 
* The actual board is:
*
* [ e m e ]
* [ e m e ]
* [ e m e ]
*
* From the user perspective, the initialized board should be:
*
* [ # # # ]
* [ # # # ]
* [ # # # ]
*
* From the user perspective, the board in the middle of a game could be:
*
* [ # # e ]
* [ # # e ]
* [ # # e ]
*
*/
"""


# import requests
# import mysql.connector
# import pandas as pd

# [
#     # # #
#     # # #
#     # # #
# ]

# [
#     [ e m e ]
#     [ e m e ]
#     [ e m e ]
# ]

# struct space {
#     bool discvoered
#     bool mine
#     # bool exploded
# }

# [
#     [ # # #]
#     [e e # ]
#     [m # # ]
#     [space space space]
# ]

# * [[ e m e ]
# *  [ e m e ]
# *  [ e m e ]]

from random import seed
from random import randint

class Space():
    def __init__(self, mine):
        self.mine = mine
        self.discovered = False

    def printSpaceSecret(self):
        if self.discovered:
            if self.mine:
                print(" m ", end = '')
            else:
                print(" e ", end='')

        else:
            print(" # ", end='')

    def printSpace(self):
        if self.mine:
            print(" m ", end = '')
        else:
            print(" e ", end='')

# This function was not ussed on the interview
def shouldHaveMine(noMines, currentNumberOfMines):
    if currentNumberOfMines == noMines:
        return False

    currentNumberOfMines += 1
    num = randint(0, 1)

    return num == 1

def fixNumberOfMines(columns, rows, noMines, board):

    currentNumberOfMines = 0

    while currentNumberOfMines < noMines:

        x = randint(0, rows - 1)
        y = randint(0, columns - 1)

        if not board[x][y].mine:
            board[x][y].mine = True
            currentNumberOfMines += 1

def minesweeper(columns, rows, noMines):

    if columns < 0 or rows < 0 or noMines < 0:
        print("Columns, rows or number of mines can not be less than 0")
        return

    if noMines > columns * rows:
        print("The number of mines is bigger that expected")
        return

    board = [[Space(False) for x in range(columns)] for i in range(rows)]
    fixNumberOfMines(columns, rows, noMines, board)

    for row in board:
        for space in row:
            space.printSpace()
        print("")
    print("")

# minesweeper(3, 3, 3)
# minesweeper(3, -3, 3)
# minesweeper(3, 3, 10)
# minesweeper(3, 4, 3)
# minesweeper(3, 4, -9)