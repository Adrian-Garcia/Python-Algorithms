"""407. Integer Replacement Problem
https://tutorialhorizon.com/algorithms/integer-replacement-problem/
"""

from typing import List


def backtracking(currNumber: int, prevChain: List[int], result: List[int]) -> List[int]:
    if len(result):
        return

    if currNumber == 1:
        result.append(prevChain + [1])
        return

    newChain = prevChain.copy()
    newChain.append(currNumber)

    if currNumber % 2 == 0:
        backtracking(currNumber // 2, newChain, result)
        return

    backtracking(currNumber - 1, newChain, result)
    backtracking(currNumber + 1, newChain, result)


def integerReplacementProblem(number: int) -> List[int]:
    result = []
    backtracking(number, [], result)
    return result.pop()


print(integerReplacementProblem(11))
