"""
Plan a round trip between two cities with minimum flight cost.

From departure city to destination city, the fees are stored in array D[].
From destination city to departure city, the fees are stored in array R[].
Both arrays should have equal length, and index corresponds to dates.

Return the indexes for the trip with minimum cost.

Example:
    
    0   1  2  3   4
D: [10, 8, 9, 11, 7], i.e represents flying on [M, Tu, W, Th, F]
R: [8,  8, 10, 7, 9]
The minimum cost will be D[1] + R[3] = 15
Return (1,3), 0-index
"""

"""
Notes:
n n log n

[10, 8, 9, 11, 7]
[8,  8, 10, 7, 9]

15
"""

from typing import List


def flights(r: List[int], d: List[int]):

    newR = []
    smallest = 99999999999
    smallestCost = 99999999999
    indexR = -1
    indexD = -1
    prevSmallest = -1

    for i, cost in enumerate(reversed(r)):
        if cost < smallest:
            smallest = cost
            prevSmallest = i

        newR.append([smallest, prevSmallest])

    newR = reversed(newR)

    for i, cost in enumerate(d):
        currCost = cost + newR[i][0]

        if currCost < smallestCost:
            indexD = i
            indexR = newR[i][1]

        smallestCost = min(smallestCost, currCost)

    return indexD, indexR
