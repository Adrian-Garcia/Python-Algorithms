"""
Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that
they add up to a given target number target and index1 < index2. Note that
index1 and index2 cannot be equal, therefore you may not use the same
element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:
    Input: numbers = [1,2,3,4], target = 3
    Output: [1,2]
    
    Explanation:
    The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array,
    index1 = 1, index2 = 2. We return [1, 2].

Constraints:
    2 <= numbers.length <= 1000
    -1000 <= numbers[i] <= 1000
    -1000 <= target <= 1000
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            low = i + 1
            top = len(numbers) - 1

            while low <= top:

                mid = (low + top) // 2

                if numbers[mid] + num == target:
                    return [i + 1, mid + 1]

                elif numbers[mid] + num < target:
                    low = mid + 1

                else:
                    top = mid - 1

        return [-1, -1]


solution = Solution()

numbers1 = [-1, 0]
target1 = -1
res1 = solution.twoSum(numbers1, target1)
print("res1", res1)

numbers2 = [-5, -3, 0, 2, 4, 6, 8]
target2 = 5
res2 = solution.twoSum(numbers2, target2)
print("res2", res2)
