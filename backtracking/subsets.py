"""
78. Subsets
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def backtracking(
        self, nums: List[int], currNums: List[int], currIndex: int, result: List[int]
    ) -> None:
        if currNums not in result:
            result.append(currNums)

        if currIndex > len(nums) - 1:
            return

        diffNums = currNums.copy()
        diffNums.append(nums[currIndex])

        self.backtracking(nums, diffNums, currIndex + 1, result)
        self.backtracking(nums, currNums, currIndex + 1, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums=nums, currNums=[], currIndex=0, result=result)

        return result


print(Solution().subsets([1, 2, 3]))
