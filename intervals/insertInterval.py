"""
                    
intervals = [[1,2],[3,5],[9,10]]

newInterval = [6,7]
currInterval = [1,2]

output = [[1,2], [3,5], []]


"""


from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        output = []

        for i, currInterval in enumerate(intervals):

            if newInterval[1] < currInterval[0]:
                output.append(newInterval)
                return output + intervals[i:]

            elif newInterval[0] > currInterval[1]:
                output.append(currInterval)

            else:
                newInterval = [
                    min(newInterval[0], currInterval[0]),
                    max(newInterval[1], currInterval[1]),
                ]

        output.append(newInterval)

        return output


solution = Solution()

intervals1 = [[1, 3], [4, 6]]
newInterval1 = [2, 5]
res1 = solution.insert(intervals1, newInterval1)
print("res1", res1)
