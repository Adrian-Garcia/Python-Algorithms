"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
        

Constraints:
    1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Using dynamic programming, you can save the previous paths taken and calculate all the taken paths.
        Uses lots of memory

        n = 4

        [
            0    [[0]],
            1    [[1], [0,1]],
            2    [[0,2], [1,2], [0,1]]
            3    [[1,3], [0,1,3], [0,2,3], [1,2,3], [0,1,3]]
        ]

        return the length of the last iteration
        """

        if n <= 2:
            return n

        stairs = [[[0]], [[1], [0, 1]]]
        curr_step = 2

        while curr_step <= n:
            stairs.append([])
            stairs[curr_step] += stairs[curr_step - 2].copy()
            stairs[curr_step] += stairs[curr_step - 1].copy()

            for path in stairs[curr_step]:
                path.append(curr_step)

            curr_step += 1

        return len(stairs[n - 1])

    def fibonacciApproach(self, n: int) -> int:
        """
        This solution cab be solved with the fibonacci sequence. Beats 100%
        """
        if n <= 2:
            return n

        nums = [1, 2]

        for i in range(2, n):
            next_num = nums[i - 2] + nums[i - 1]
            nums.append(next_num)

        return nums[len(nums) - 1]


solution = Solution()
res1 = solution.climbStairs(5)
print("res1", res1)
