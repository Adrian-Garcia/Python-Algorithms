"""
120. Triangle
https://leetcode.com/problems/triangle/solutions/7221419/recursive-dp-vs-iterative-dp-with-o-1-space-beats-100/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on 
index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:

       2
      3 4
     6 5 7
    4 1 8 3
    
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
    Input: triangle = [[-10]]
    Output: -10
 
Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -104 <= triangle[i][j] <= 104
"""


class Solution:
    def __checkMinPath(
        self,
        triangle: list[list[int]],
        curr_level: int,
        curr_position: int,
        curr_sum: int,
        result: list[int],
    ):
        curr_sum += triangle[curr_level][curr_position]

        if curr_level == len(triangle) - 1:
            result[0] = min(result[0], curr_sum)

        else:
            self.__checkMinPath(
                triangle, curr_level + 1, curr_position, curr_sum, result
            )
            self.__checkMinPath(
                triangle, curr_level + 1, curr_position + 1, curr_sum, result
            )

    def minimumTotalRecursive(self, triangle: list[list[int]]) -> int:
        result = [1000000000000]
        self.__checkMinPath(triangle, 0, 0, 0, result)
        return result[0]

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        result = 10000000000000
        positions = [[0, 0, 0]]

        while len(positions):
            level, position, prev_sum = positions.pop()

            curr_sum = prev_sum + triangle[level][position]

            if level == len(triangle) - 1:
                result = min(result, curr_sum)

            else:
                positions.append([level + 1, position, curr_sum])
                positions.append([level + 1, position + 1, curr_sum])

        return result


solution = Solution()

triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
res1 = solution.minimumTotal(triangle1)
print("res1", res1)
