"""
Valid Perfect Square
	Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
	Input: num = 16
	Output: true

Example 2:
	Input: num = 14
	Output: false
 

Constraints:
	1 <= num <= 2^31 - 1
"""


class Solution(object):
    def isPerfectSquare(self, num):
        return True if num**0.5 - int(num**0.5) == 0 else False


sol = Solution()
print(sol.isPerfectSquare(14))
