"""Longest Consecutive Sequence
https://neetcode.io/problems/longest-consecutive-sequence

Given an array of integers nums, return the length of the longest consecutive
sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly
1 greater than the previous element. The elements do not have to be consecutive
in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [2,20,4,10,3,4,5]
    Output: 4
    Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
    Input: nums = [0,3,2,5,4,6,1,1]
    Output: 7

Constraints:
    0 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(set(nums))

        biggestCount = 1
        currCount = 1

        for i in range(len(sortedNums) - 1):
            currNum = sortedNums[i]
            nextNum = sortedNums[i + 1]

            if currNum + 1 == nextNum:
                currCount += 1

            else:
                biggestCount = max(biggestCount, currCount)
                currCount = 1

        return max(biggestCount, currCount)


solution = Solution()

nums1 = [2, 20, 4, 10, 3, 4, 5]
res1 = solution.longestConsecutive(nums1)

nums2 = [0, 3, 2, 5, 4, 6, 1, 1]
res2 = solution.longestConsecutive(nums2)

print("res1", res1)
print("res2", res2)
