"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

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

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = self.permute(nums[1:])
        res = []

        for permutation in permutations:
            for i in range(len(permutation) + 1):
                permutation_copy = permutation.copy()
                permutation_copy.insert(i, nums[0])
                res.append(permutation_copy)

        return res

        
solution = Solution()

nums1 = [1,2,3]
res1 = solution.permute(nums1)
print("res1", res1)
