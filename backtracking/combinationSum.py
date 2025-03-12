"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list
of all unique combinations of candidates where the chosen numbers sum to target. You may
return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers is
different.

The test cases are generated such that the number of unique combinations that sum up to
target is less than 150 combinations for the given input.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40

"""

from typing import List
import itertools


class Solution:
    def getCombinationsThatSumTarget(
        selff, nums, currCombination, target, result, currAddition, index
    ):
        if index >= len(nums):
            return

        newElement = nums[index]

        if currAddition + newElement == target:
            result.append(currCombination + [newElement])

        newCurr = currCombination + [newElement]

        selff.getCombinationsThatSumTarget(
            nums, newCurr, target, result, currAddition + newElement, index + 1
        )
        selff.getCombinationsThatSumTarget(
            nums, currCombination, target, result, currAddition, index + 1
        )

    def deleteDuplicatesFromResult(self, result):
        for i in range(len(result)):
            result[i] = sorted(result[i])

        result.sort()
        return list(result for result, _ in itertools.groupby(result))

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        result = []
        self.getCombinationsThatSumTarget(nums, [], target, result, 0, 0)
        return self.deleteDuplicatesFromResult(result)

    def backtrackingDoesNotWork(
        self,
        candidates: List[int],
        target: int,
        currSum: int,
        result: List[int],
        currCandidates: List[int],
        currIndex: int,
    ) -> None:
        print(currCandidates)

        if currSum == target and currCandidates not in result:
            result.append(currCandidates)

        if currIndex > len(candidates) - 1:
            return

        currNum = candidates[currIndex]
        diffCandidates = currCandidates.copy()
        diffCandidates.append(currNum)
        newSum = currSum + currNum

        self.backtracking(
            candidates, target, newSum, result, diffCandidates, currIndex + 1
        )
        self.backtracking(
            candidates, target, currSum, result, currCandidates, currIndex + 1
        )

    def combinationSumDoesNotWork(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        result = []
        self.backtracking(
            candidates=candidates,
            target=target,
            currSum=0,
            result=result,
            currCandidates=[],
            currIndex=0,
        )

        return result


print(Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
