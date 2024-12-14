''' Question 1: 2D Spiral Array
https://www.facebook.com/careers/life/sample_interview_questions

Find the pattern and complete the function:
    int[][] spiral(int n);
    where n is the size of the 2D array.

Sample Result

    input = 3
        123
        894
        765

    input = 4
        01 02 03 04
        12 13 14 05
        11 16 15 06
        10 09 08 07

    input = 8
        1 2 3 4 5 6 7 8
        28 29 30 31 32 33 34 9
        27 48 49 50 51 52 35 10
        26 47 60 61 62 53 36 11
        25 46 59 64 63 54 37 12
        24 45 58 57 56 55 38 13
        23 44 43 42 41 40 39 14
        22 21 20 19 18 17 16 15
'''
from typing import List

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = "\t")
        print()

def spiral(n: int) -> List[List[int]]:
    matrix = [["F"] * n for _ in range(n)]

    count = 1
    i = 0
    j = 0

    limit = n * n
    status = "j+"

    while count <= limit:

        if status == "j+":
            while j < n and matrix[i][j] == "F":
                matrix[i][j] = count
                count += 1
                j += 1
            
            j -= 1
            i += 1

            status = "i+"

        elif status == "i+":
            while i < n and matrix[i][j] == "F":
                matrix[i][j] = count
                count += 1
                i += 1
            
            i -= 1
            j -= 1

            status = "j-"

        elif status == "j-":
            while j >= 0 and matrix[i][j] == "F":
                matrix[i][j] = count
                count += 1
                j -= 1

            j += 1
            i -= 1

            status = "i-"

        elif status == "i-":
            while i >= 0 and matrix[i][j] == "F":
                matrix[i][j] = count
                count += 1
                i -= 1

            i += 1
            j += 1
            status = "j+"

        printMatrix(matrix)
        print()

    return matrix

printMatrix(spiral(7))
