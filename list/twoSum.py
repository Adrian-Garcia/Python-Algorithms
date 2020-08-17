"""
Two Sum

	Given an array of integers, return indices of the two numbers such that they add up to a specific 
	target.
	
	You may assume that each input would have exactly one solution, and you may not use the same
	element twice.

Example:
	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
"""

class Solution(object):

	def checkEdges(self, arr, position):

		if position != len(arr)-1 and position != 0:
			if arr[position] == arr[position+1] or arr[position] == arr[position-1]:
				return True

		elif position == 0:
			if arr[position] == arr[position+1]:
			 	return True
		
		else:
			if arr[position] == arr[position-1]:
			 	return True

		return False

	def binarySearch(self, arr, target):

		low = 0
		top = len(arr) - 1

		while low <= top:

			mid = (top + low) // 2

			if arr[mid] < target:
				low = mid + 1

			elif arr[mid] > target:
				top = mid - 1

			else:
				return mid

		return -1

	def twoSum(self, nums, target):

		myNewArr = nums.copy()
		myNewArr.sort()

		for i in range(len(nums)):
			targetNum = target - nums[i]

			result = self.binarySearch(myNewArr, targetNum)

			if (result != -1):

				if targetNum == target/2:

					if self.checkEdges(nums, result):
						return [i, result]

				return [i, result]

		return [-1,-1]


sol = Solution()
print(sol.twoSum([1,2,3], 5))