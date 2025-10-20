"""
238. Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

 

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    - 2 <= nums.length <= 105
    - -30 <= nums[i] <= 30
    - The input is generated such that answer[i] is guaranteed to fit in a
    32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []

        for i in range(len(nums)):
            num = nums[i]
            prefix.append(num) if i == 0 else prefix.append(num * prefix[i - 1])

        for i in range(len(nums), 0, -1):
            num = nums[i - 1]
            postfix.append(num) if i == len(nums) else postfix.append(num * postfix[-1])

        postfix = list(reversed(postfix))

        for i in range(len(nums)):
            pre = 1 if i == 0 else prefix[i - 1]
            post = 1 if i == len(nums) - 1 else postfix[i + 1]

            result.append(pre * post)

        return result


solution = Solution()

nums1 = [1, 2, 3, 4]
res1 = solution.productExceptSelf(nums1)

print("res1", res1)
