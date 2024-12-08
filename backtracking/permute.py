"""46. Permutations
https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]
 

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

from typing import List


class Solution:
    def __dfs(
        self, nums: List[int], prevNum: int, result: List[int], originalLen: int
    ) -> List[int]:
        print("nums", nums)
        print("prevNum", prevNum)
        print("result", result)
        print()

        if len(nums) == 1:
            return nums.append(prevNum)

        for i in range(len(nums)):
            num = nums[i]
            subNums = nums.copy()
            del subNums[i]
            permutation = self.__dfs(subNums, num, result, originalLen)
            print("permutation", permutation)
            print("subNums", subNums)
            print("num", num)
            print("result", result)
            if len(permutation) == originalLen:
                result.append(permutation)

        return []

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.__dfs(nums, None, result, len(nums))

        return result


nums = [1, 2, 3]
print("result", Solution().permute(nums))
