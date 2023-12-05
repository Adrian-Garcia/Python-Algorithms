"""
229. Majority Element II
Medium
Given an integer array of size n, find all elements that appear more than 
⌊ n/3 ⌋ times.

Example 1:
    Input: nums = [3,2,3]
    Output: [3]

Example 2:
    Input: nums = [1]
    Output: [1]

Example 3:
    Input: nums = [1,2]
    Output: [1,2]

Constraints:
    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution(object):
    def majorityElement(self, nums):
        nums_counter = dict()
        big_numbers = list()

        for num in nums:
            if num in nums_counter:
                nums_counter[num] += 1

            else:
                nums_counter[num] = 1

        for num in nums_counter:
            if nums_counter[num] > len(nums) // 3:
                big_numbers.append(num)

        return big_numbers


nums = [1, 2, 3]
solution = Solution()
majorityElement = solution.majorityElement(nums)
print("majorityElement:", majorityElement)
