"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).You have to rotate the image in-place, which means you have
to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
 
Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> None:
        """
        [1,2,3]    [1,4,7]
        [4,5,6] => [2,5,8]
        [7,8,9]    [3,6,9]
        """

        matrixSize = len(matrix)
        for i in range(matrixSize):
            for j in range(i + 1, matrixSize):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix: List[List[int]]) -> None:
        """
        [1,4,7]    [7,4,1]
        [2,5,8] => [8,5,2]
        [3,6,9]    [9,6,3]
        """
        matrixSize = len(matrix)
        for i in range(matrixSize):
            for j in range(matrixSize // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Solution().rotate(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()
