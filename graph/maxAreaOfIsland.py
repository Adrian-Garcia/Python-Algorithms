"""
695. Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing
land) connected 4-directionally (horizontal or vertical.) You may assume all four
edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
    Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    Output: 6

    Explanation:
        The answer is not 11, because the island must be connected 4-directionally.

Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""

from typing import List


class Solution:
    def __getSizeOfIsland(
        self,
        grid: List[List[int]],
        iPosition: int,
        jPosition: int,
        iSize: int,
        jSize: int,
    ) -> int:

        queue = [[iPosition, jPosition]]
        islandSize = 0

        while len(queue):
            i, j = queue.pop()

            if grid[i][j] == 1:
                islandSize += 1
                grid[i][j] = 2

            # up
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                queue.append([i - 1, j])

            # down
            if i + 1 < iSize and grid[i + 1][j] == 1:
                queue.append([i + 1, j])

            # left
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                queue.append([i, j - 1])

            # right
            if j + 1 < jSize and grid[i][j + 1] == 1:
                queue.append([i, j + 1])

        return islandSize

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not len(grid):
            return 0

        maxIslandSize = 0

        iSize = len(grid)
        jSize = len(grid[0])

        for i in range(iSize):
            for j in range(jSize):
                currPosition = grid[i][j]

                if currPosition == 1:
                    currIslandSize = self.__getSizeOfIsland(grid, i, j, iSize, jSize)

                    maxIslandSize = max(maxIslandSize, currIslandSize)

        return maxIslandSize


solution = Solution()

grid1 = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
res1 = solution.maxAreaOfIsland(grid1)
print("res1", res1)

grid2 = [[1, 1, 1, 1, 1]]
res2 = solution.maxAreaOfIsland(grid2)
print("res2", res2)
