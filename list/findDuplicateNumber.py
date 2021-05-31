"""
Find the Duplicate Number
	Given an array nums containing n + 1 integers where each integer is
	between 1 and n (inclusive), prove that at least one duplicate
	number must exist. Assume that there is only one duplicate number,
	find the duplicate one.

Example 1:
	Input: [1,3,4,2,2]
	Output: 2

Example 2:
	Input: [3,1,3,4,2]
	Output: 3

Note:
	1. You must not modify the array (assume the array is read only).
	2. You must use only constant, O(1) extra space.
	3. Your runtime complexity should be less than O(n2).
	4. There is only one duplicate number in the array, but it could be
		 repeated more than once.
"""


class Solution(object):

    """
    Floyd's Tortoise and Hare
            Runtime: 40 ms, faster than 99.73% of Python online submissions for Find the Duplicate Number.
            Memory Usage: 14.6 MB, less than 42.52% of Python online submissions for Find the Duplicate Number.
    """

    def findDuplicate0(self, nums):

        tortoise = nums[0]
        hare = nums[0]

        while True:

            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        ptr1 = nums[0]
        ptr2 = tortoise

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

    """
	Sorting
		Runtime: 52 ms, faster than 81.45% of Python online submissions for Find the Duplicate Number.
		Memory Usage: 14.5 MB, less than 78.41% of Python online submissions for Find the Duplicate Number.
	"""

    def findDuplicate(self, nums):

        nums.sort()

        for i in range(len(nums) - 1):

            j = i + 1
            if nums[i] == nums[j]:
                return nums[i]


sol = Solution()
print(sol.findDuplicate([3, 1, 3, 4, 2]))
