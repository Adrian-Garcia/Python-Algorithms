"""
# Sudoku Validator Problem. 
# Tell me whether a given Sudoku board is valid or invalid.

# Rules of Sudoku:
#   no duplicate 1-9 in any row
#   no duplicate 1-9 in any column
#   no duplicate 1-9 in any 3x3 square
"""

"""

Set(1, 5)
list[1, ,0 , 0, 0, 1 ... 9]

"""
from typing import List
valid_final_board = [
    [1, 5, 2,   4, 8, 9,   3, 7, 6],
    [7, 3, 9,   2, 5, 6,   8, 4, 1],
    [4, 6, 8,   3, 7, 1,   2, 9, 5],
    [3, 8, 7,   1, 2, 4,   6, 5, 9],
    [5, 9, 1,   7, 6, 3,   4, 2, 8],
    [2, 4, 6,   8, 9, 5,   7, 1, 3],
    [9, 1, 4,   6, 3, 7,   5, 8, 2],
    [6, 2, 5,   9, 4, 8,   1, 3, 7],
    [8, 7, 3,   5, 1, 2,   9, 6, 4],
]


final_board = [
    [1, 5, 2,   4, 8, 9,   3, 7, 6],
    [7, 3, 9,   2, 5, 6,   8, 4, 1],
    [4, 6, 8,   3, 7, 1,   2, 9, 5],
    [3, 8, 7,   1, 2, 4,   6, 5, 9],
    [5, 9, 1,   7, 6, 3,   4, 2, 8],
    [2, 4, 6,   8, 9, 5,   7, 1, 3],
    [9, 1, 4,   6, 3, 7,   5, 8, 2],
    [6, 2, 5,   9, 4, 8,   1, 3, 7],
    [8, 7, 3,   5, 1, 2,   9, 6, 4],
]

broken_rows = [
    [7, 5, 2,   4, 8, 9,   3, 7, 6],
    [1, 3, 9,   2, 5, 6,   8, 4, 1],
    [4, 6, 8,   3, 7, 1,   2, 9, 5],
    [3, 8, 7,   1, 2, 4,   6, 5, 9],
    [5, 9, 1,   7, 6, 3,   4, 2, 8],
    [2, 4, 6,   8, 9, 5,   7, 1, 3],
    [9, 1, 4,   6, 3, 7,   5, 8, 2],
    [6, 2, 5,   9, 4, 8,   1, 3, 7],
    [8, 7, 3,   5, 1, 2,   9, 6, 4],
]
broken_columns = [
    [5, 1, 2,   4, 8, 9,   3, 7, 6],
    [7, 3, 9,   2, 5, 6,   8, 4, 1],
    [4, 6, 8,   3, 7, 1,   2, 9, 5],
    [3, 8, 7,   1, 2, 4,   6, 5, 9],
    [5, 9, 1,   7, 6, 3,   4, 2, 8],
    [2, 4, 6,   8, 9, 5,   7, 1, 3],
    [9, 1, 4,   6, 3, 7,   5, 8, 2],
    [6, 2, 5,   9, 4, 8,   1, 3, 7],
    [8, 7, 3,   5, 1, 2,   9, 6, 4],
]
broken_squares = [
    [1, 2, 3,   4, 5, 6,   7, 8, 9],
    [9, 1, 2,   3, 4, 5,   6, 7, 8],
    [8, 9, 1,   2, 3, 4,   5, 6, 7],
    [7, 8, 9,   1, 2, 3,   4, 5, 6],
    [6, 7, 8,   9, 1, 2,   3, 4, 5],
    [5, 6, 7,   8, 9, 1,   2, 3, 4],
    [4, 5, 6,   7, 8, 9,   1, 2, 3],
    [3, 4, 5,   6, 7, 8,   9, 1, 2],
    [2, 3, 4,   5, 6, 7,   8, 9, 1],
]

final_board = [
    [1, 5, 0,   2, 8, 9,   3, 7, 6],
    [7, 3, 9,   2, 5, 6,   8, 4, 1],
    [4, 6, 8,   3, 7, 1,   2, 9, 5],
    [3, 8, 7,   1, 2, 4,   6, 5, 9],
    [5, 9, 1,   7, 6, 3,   4, 2, 8],
    [2, 4, 6,   8, 9, 5,   7, 1, 3],
    [9, 1, 4,   6, 3, 7,   5, 8, 2],
    [6, 2, 5,   9, 4, 8,   1, 3, 7],
    [8, 7, 3,   5, 1, 2,   9, 6, 4],
]


def validateRows(sudoku: List[List[int]]) -> bool:
    for i in range(len(sudoku)):
        nums = [0] * 9
        for j in range(len(sudoku[i])):
            if nums[sudoku[i][j] - 1] != 0:
                return False
            nums[sudoku[i][j] - 1] += 1
        if sum(nums) != 9:
            return False
    return True


def validateColumns(sudoku: List[List[int]]) -> bool:
    for i in range(len(sudoku)):
        nums = [0] * 9
        for j in range(len(sudoku[i])):
            if nums[sudoku[j][i] - 1] != 0:
                return False
            nums[sudoku[j][i] - 1] += 1
        if sum(nums) != 9:
            return False
    return True


def validateSubMatrix(sudoku: List[List[int]]) -> bool:
    for a in range(3):
        for b in range(3):
            nums = [0] * 9

            for i in range(3):
                for j in range(3):
                    indexI = i + a * 3
                    indexJ = j + b * 3

                    # print(sudoku[indexI][indexJ], end=" ")
                    # print(indexI, " ", indexJ, end="")

                    if nums[sudoku[indexI][indexJ] - 1] != 0:
                        return False
                    nums[sudoku[indexI][indexJ] - 1] += 1

                # print()

            if sum(nums) != 9:
                return False
    return True


def sudokuValidator(sudoku: List[List[int]]) -> bool:
    rows = validateRows(sudoku)
    cols = validateColumns(sudoku)
    square = validateSubMatrix(sudoku)

    print("rows", rows)
    print("cols", cols)
    print("square", square)

    return validateRows(sudoku) and validateColumns(sudoku) and validateSubMatrix(sudoku)


result = sudokuValidator(broken_squares)
print("result", result)
