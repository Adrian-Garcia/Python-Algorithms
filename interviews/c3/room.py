"""
You are given an m x n matrix of square spaces and each of these spaces can
have 3 possible values:
  - -1: Represents a water body which you cannot travel through.
  - 0: Represents a door. 
  - int_max: Represents an empty space. 

Return the distance from the top leftmost empty space to the closest door.
Assume that the maximum distance between this space and door is less than
int_max

Example:
Input:
  [[ int_max  -1     0      int_max]
  [ int_max int_max int_max   -1   ]
  [ int_max int_max int_max   -1   ]
  [   0        -1   int_max int_max]]
  Each cell of this matrix represents a square space. 

Output:
  3
"""


def get_new_positions(i, j, top_right, top_down, visited):
    result = []

    if i + 1 < top_right and not visited[i + 1][j]:
        result.append([i + 1, j])

    if i - 1 >= 0 and not visited[i - 1][j]:
        result.append([i - 1, j])

    if j + 1 < top_down and not visited[i][j + 1]:
        result.append([i, j + 1])

    if j - 1 >= 0 and not visited[i][j - 1]:
        result.append([i, j - 1])

    return result


def BFS(matrix):

    if not matrix:
        return -1

    queue = [[0, 0]]
    distances = [0]

    top_right = len(matrix)
    top_down = len(matrix[0])

    visited = [[False] * top_right] * top_down

    while queue:
        i, j = queue.pop(0)
        curr_distance = distances.pop(0)
        visited[i][j] = True
        curr = matrix[i][j]

        if curr == 0:
            return curr_distance

        elif curr == -1:
            continue

        new_positions = get_new_positions(i, j, top_right, top_down, visited)
        queue += new_positions
        distances += len(new_positions) * [curr_distance + 1]

    return -1


int_max = 10000
matrix = [
    [int_max, -1, 0, int_max],
    [int_max, int_max, int_max, -1],
    [int_max, int_max, int_max, -1],
    [0, -1, int_max, int_max],
]

result = BFS(matrix)
print(result)
