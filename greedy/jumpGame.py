"""
Jump Game
https://neetcode.io/problems/jump-game

You are given an integer array nums where each element nums[i] indicates your maximum
jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:
    Input: nums = [1,2,0,1,0]
    Output: true

    Explanation:
        First jump from index 0 to 1, then from index 1 to 3, and lastly from index
        3 to 4.

Example 2:
    Input: nums = [1,2,1,0,1]
    Output: false

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        queue = [0]
        visited = set()
        while queue:
            currPosition = queue.pop(0)

            if currPosition == len(nums) - 1:
                return True

            if currPosition in visited or currPosition >= len(nums) or currPosition < 0:
                continue

            visited.add(currPosition)
            jumpSize = nums[currPosition]
            farestPosition = currPosition + jumpSize

            minPos = min(currPosition, farestPosition)
            maxPos = max(currPosition, farestPosition)

            jumpRange = list(range(minPos, maxPos + 1))

            queue += jumpRange

        return False


solution = Solution()

nums1 = [1, 2, 0, 1, 0]
res1 = solution.canJump(nums1)
print("res1", res1)

nums2 = [1, 2, 1, 0, 1]
res2 = solution.canJump(nums2)
print("res2", res2)
