""" Not finished
Daily Temperatures
https://neetcode.io/problems/daily-temperatures

You are given an array of integers temperatures where temperatures[i]
represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the
ith day before a warmer temperature appears on a future day. If there is
no day in the future where a warmer temperature will appear for the ith
day, set result[i] to 0 instead.

Example 1:
    Input: temperatures = [30,38,30,36,35,40,28]
    Output: [1,4,1,2,1,0,0]

Example 2:
    Input: temperatures = [22,21,20]
    Output: [0,0,0]

Constraints:
    1 <= temperatures.length <= 1000.
    1 <= temperatures[i] <= 100
"""
from typing import List
import heapq


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        [30, 38, 30, 36, 35, 40, 28]

        maxVal =

        """

        heap = []  # 40    28
        result = []  # 0     0

        for temperature in reversed(temperatures):
            heapq._heapify_max(heap)
            popedValues = []
            count = 0

            print("temperature  ", temperature)
            print("heap         ", heap)
            while heap:

                maxVal = heapq.heappop(heap)
                popedValues.append(maxVal)

                print("maxVal       ", maxVal)

                if maxVal < temperature:
                    break

                count += 1

            print("count        ", count)
            print()

            heap += popedValues
            heap.append(temperature)
            result.append(count)

        return list(reversed(result))


solution = Solution()

temperatures1 = [30, 38, 30, 36, 35, 40, 28]
res1 = solution.dailyTemperatures(temperatures1)

print(res1)
