"""	Not finished
Sum of Square Numbers
	Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
	Input: 5
	Output: True
	Explanation: 1 * 1 + 2 * 2 = 5
 
Example 2:
	Input: 3
	Output: False
"""


def isPerfectSquare(num):
    return True if num ** 0.5 - int(num ** 0.5) == 0 else False


class Solution(object):
    def judgeSquareSum(self, c):

        if c == 2:
            return True

        if c == 1:
            return False

        for i in range(c - 1):

            if isPerfectSquare(c - (i * i)):
                return True

        return False


sol = Solution()
print(sol.judgeSquareSum(3))
