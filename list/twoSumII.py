"""167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not
use the same element twice.

Your solution must use only constant extra space.

Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]

    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
    return [1, 2].

Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    
    Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
    return [1, 3].

Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    
    Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
    return [1, 2].
 
Constraints:
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""

from typing import List


class Solution:
    def __binarySearch(self, numbers, needed, i):
        low = 0
        top = len(numbers) - 1

        while low <= top:
            mid = (top + low) // 2

            if numbers[mid] < needed:
                low = mid + 1

            elif numbers[mid] > needed:
                top = mid - 1

            else:
                if mid != i:
                    return mid

                if mid + 1 < len(numbers) and numbers[mid + 1] == needed:
                    return mid + 1

                if mid - 1 >= 0 and numbers[mid - 1] == needed:
                    return mid - 1

                return -1

        return -1

    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        # Solution accepted but is very slow O(n log n)
        for i in range(len(numbers)):
            num = numbers[i]
            needed = target - num
            foundIndex = self.__binarySearch(numbers, needed, i)

            if foundIndex != -1:
                return [i + 1, foundIndex + 1]

        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Uses two pointers (does not work) O(n)
        i = 0
        j = len(numbers) - 1

        while i < len(numbers) and j < len(numbers):
            result = numbers[i] + numbers[j]

            if result == target:
                return [min(i + 1, j + 1), max(i + 1, j + 1)]

            if result > target:
                j -= 1

            if result < target:
                i += 1
                j = i + 1


numbers1 = [2, 7, 11, 15]
solution1 = Solution().twoSum(numbers1, 9)
print(solution1)

numbers2 = [5, 25, 75]
solution2 = Solution().twoSum(numbers2, 100)
print(solution2)
