""" Not finished
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12


Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200
"""


class Solution(object):
    def __getUpLeftValues(self, grid, i, j):
        up = grid[i - 1][j] if i - 1 >= 0 else 400
        left = grid[i][j - 1] if j - 1 >= 0 else 400

        return up, left

    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if (i, j) != (0, 0):
                    up, left = self.__getUpLeftValues(grid, i, j)
                    grid[i][j] += min(up, left)

        return grid[rows - 1][cols - 1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

solution = Solution()
minPathSum = solution.minPathSum(grid)
print(minPathSum)
