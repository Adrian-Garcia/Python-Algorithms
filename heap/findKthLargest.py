"""
Kth Largest Element in an Array
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:
    Input: nums = [2,3,1,5,4], k = 2
    Output: 4

Example 2:
    Input: nums = [2,3,1,1,5,5,4], k = 3
    Output: 4

Constraints:
    1 <= k <= nums.length <= 10000
    -1000 <= nums[i] <= 1000
"""
from typing import List
import heapq

class Solution:

    # Does not work for negative numbers
    def findKthLargestCountSort(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = [0] * (max_val + 1)

        while len(nums) > 0:
            num = nums.pop(0)
            count[num] += 1

        for i in range(len(count)):
            while count[i] > 0:
                nums.append(i)
                count[i] -= 1

        nums = list(reversed(nums))

        return nums[k-1]

    # Works but slow
    def findKthLargestHeapSolution(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        count = 1

        while count <= k:
            heapq._heapify_max(nums)
            response = heapq.heappop(nums)
            count += 1

        return response
    

solution = Solution()

nums1 = [2,3,1,5,4]
res1 = solution.findKthLargest(nums1, 2)
print("res1", res1)

nums2 = [2,3,1,1,5,5,4]
res2 = solution.findKthLargest(nums2, 1)
print("res1", res1)
