"""
169. Majority Element
Easy
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        nums_counter = dict()
        big_number = -1
        big_counter = -1

        for num in nums:
            if num in nums_counter:
                nums_counter[num] += 1

            else:
                nums_counter[num] = 1

            if nums_counter[num] > big_counter:
                big_number = num
                big_counter = nums_counter[num]

        return big_number

    def majorityElementConstantSpace(self, nums):
        nums_counter = Counter(nums)
        return max(nums_counter, key=nums_counter.get)


nums = [3, 2, 3]
solution = Solution()
majorityElement = solution.majorityElementConstantSpace(nums)
print("majorityElement:", majorityElement)
