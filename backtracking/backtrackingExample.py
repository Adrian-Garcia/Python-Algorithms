from typing import List


def backtracking(
    nums: List[int], currNums: List[int], currIndex: int, result: List[int]
) -> None:
    if currNums not in result:
        result.append(currNums)

    if currIndex > len(nums) - 1:
        return

    diffNums = currNums.copy()
    diffNums.append(nums[currIndex])

    backtracking(nums, diffNums, currIndex + 1, result)
    backtracking(nums, currNums, currIndex + 1, result)


def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    backtracking(nums=nums, currNums=[], currIndex=0, result=result)

    return result


print(subsets([1, 2, 3]))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
