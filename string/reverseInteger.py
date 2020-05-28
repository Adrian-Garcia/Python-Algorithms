'''
Reverse Integer
	Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
	Input: 123
	Output: 321

Example 2:
	Input: -123
	Output: -321

Example 3:
	Input: 120
	Output: 21

Note:
	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
	[−231,  231 − 1]. 

	For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution(object):
	
	def reverse(self, x):

		strNum = str(x)
		positive = True if x >= 0 else False

		if (not positive):
			strNum = strNum[:0] + strNum[0+1:]

		strNum = strNum [::-1]

		result = int(strNum)

		if (result > 2**31-1):
			return 0

		if (positive):
			return result

		return result * -1

sol = Solution()
print(sol.reverse(1534236469))