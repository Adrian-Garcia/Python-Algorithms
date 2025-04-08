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
