"""
Missing Number
	Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
	find the one that is missing from the array.

Example 1:
	Input: [3,0,1]
	Output: 2

Example 2:
	Input: [9,6,4,2,3,5,7,0,1]
	Output: 8

Note:
	Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution(object):

    # First solution beats 77%
    def missingNumber(self, nums):

        found = [False] * (len(nums) + 1)

        for i in nums:
            found[i] = True

        for i in range(len(found)):
            if found[i] == False:
                return i


sol = Solution()
print(sol.missingNumber([3, 0, 1]))
