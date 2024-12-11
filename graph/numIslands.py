"""408. Number of Islands
https://tutorialhorizon.com/algorithms/number-of-islands/

Objective: Given a 2d grid map of '1's (land) and '0's (water), count the number
of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. Assume all four edges of the grid are
all surrounded by water. Given such a grid, write an algorithm to find the
number of islands in it.

Example 1:
    Input:
        11110
        11010
        11000
        00000
    No of Islands: 1

Example 2:
    Input:
        11000
        11000
        00100
        00011
    No of Islands: 3

Example 3:
    Input:
        11110
        00010
        00010
        11110
    No of Islands: 1
"""

from typing import List


def getAdjacentPositions(map, i, j, lenI, lenJ) -> List:
    result = []

    # Left
    if i - 1 >= 0 and map[i - 1][j] == 1:
        result.append((i - 1, j))

    # Right
    if i + 1 < lenI and map[i + 1][j] == 1:
        result.append((i + 1, j))

    # Up
    if j - 1 >= 0 and map[i][j - 1] == 1:
        result.append((i, j - 1))

    # Down
    if j + 1 < lenJ and map[i][j + 1] == 1:
        result.append((i, j + 1))

    return result


def visitIsland(map, iPosition, jPosition, lenI, lenJ) -> None:
    queue = [(iPosition, jPosition)]

    while len(queue):
        i, j = queue.pop()
        map[i][j] = 2
        queue += getAdjacentPositions(map, i, j, lenI, lenJ)


def numIslands(map: List[List[int]]):
    numOfIslands = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            currPosition = map[i][j]

            if currPosition == 1:
                visitIsland(map, i, j, len(map), len(map[i]))
                numOfIslands += 1

    return numOfIslands


map0 = [[1, 0], [0, 1]]

map1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]

map2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]

map3 = [[1, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0]]

print(numIslands(map3))
