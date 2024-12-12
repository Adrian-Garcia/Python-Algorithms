"""457. Given an array, print all unique subsets with a given sum.
https://tutorialhorizon.com/algorithms/given-an-array-print-all-unique-subsets-with-a-given-sum/
"""

from typing import List
import numpy as np
import itertools


def getCombinations(
    arr: List[int], i: int, currentSubset: List[int], result: List[int]
) -> List[List[int]]:
    newSubset = currentSubset.copy()
    result.append(newSubset)

    # Uncomment this if you want to avoid using itertools
    # if newSubset not in result:
    #    result.append(newSubset)

    if i >= len(arr):
        return

    getCombinations(arr, i + 1, newSubset + [arr[i]], result)
    getCombinations(arr, i + 1, newSubset, result)


def getValidCombinations(
    combinations: List[List[int]], targetSum: int
) -> List[List[int]]:
    result = []

    # Comment this if you want to avoid using itertools
    combinations.sort()
    combinations = list(k for k, _ in itertools.groupby(combinations))

    for combination in combinations:
        if np.sum(combination) == targetSum:
            result.append(combination)

    return result


def combinationUtil(arr: List[int], targetSum: int) -> List[List[int]]:
    combinations = []
    getCombinations(arr, 0, [], combinations)
    return getValidCombinations(combinations, targetSum)


arr0 = [1, 2, 3]
print(combinationUtil(arr0, 3))
