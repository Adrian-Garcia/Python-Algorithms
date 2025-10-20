"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""

from typing import List


class Solution:
    def __getRanges(self, matrix):
        ranges = []

        for row in matrix:
            end = len(row) - 1
            ranges.append([row[0], row[end]])

        return ranges

    def __findRow(self, matrix, target):
        ranges = self.__getRanges(matrix)

        low = 0
        top = len(ranges) - 1

        while low <= top:

            mid = (top + low) // 2

            start, end = ranges[mid]

            if start <= target <= end:
                return mid

            elif target > end:
                low = mid + 1

            else:
                top = mid - 1

        return -1

    def __findBinary(self, row, target):
        low = 0
        top = len(row) - 1

        while low <= top:
            mid = (top + low) // 2

            if row[mid] < target:
                low = mid + 1

            elif row[mid] > target:
                top = mid - 1

            else:
                return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.__findRow(matrix, target)
        if row == -1:
            return False
        return self.__findBinary(matrix[row], target)


solution = Solution()

matrix1 = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target1 = 15
res1 = solution.searchMatrix(matrix1, target1)
print("res1", res1)
