"""
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
    Input: board = 
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

Example 2:
    Input: board = 
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two
    8's in the top left 3x3 sub-box, it is invalid.
"""

from typing import List


class Solution:
    SUDOKU_LENGTH = 9

    def checkRows(self, board: List[List[str]]) -> bool:
        for i in range(Solution.SUDOKU_LENGTH):
            numsInRow = set()

            for j in range(Solution.SUDOKU_LENGTH):
                space = board[i][j]

                if space != "." and space in numsInRow:
                    return False

                numsInRow.add(space)

        return True

    def checkCols(self, board: List[List[str]]) -> bool:
        for i in range(Solution.SUDOKU_LENGTH):
            numsInCol = set()

            for j in range(Solution.SUDOKU_LENGTH):
                space = board[j][i]

                if space != "." and space in numsInCol:
                    return False

                numsInCol.add(space)

        return True

    def checkSquares(self, board: List[List[str]]) -> bool:
        for i in range(3):
            numsInSquare = set()

            for j in range(3):
                space = board[3 * i + i][3 * i + j]

                if space != "." and space in numsInSquare:
                    return False

                numsInSquare.add(space)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.checkRows(board)
            and self.checkCols(board)
            and self.checkSquares(board)
            # self.checkRows(board)
            # and self.checkCols(board)
        )


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]


print(Solution().isValidSudoku(board))
