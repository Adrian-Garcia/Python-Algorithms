"""
Write a function that, given a list and a target sum, returns zero-based indices of any two
distinct elements whose sum is equal to the target sum. If there are no such elements, the
function should return None. Ex.: findTwoSum([1,3,5,7,9,6], 12)  -> [(1,4),(2,3)]
"""


def populate_dict(nums):
    dictNums = dict()
    for i in range(len(nums)):
        num = nums[i]
        dictNums[num] = i

    return dictNums


def findTwoSum(nums, target):
    dictNums = populate_dict(nums)
    combinations = set()

    for i in range(len(nums)):
        num = nums[i]
        candidate = target - num

        if candidate in dictNums and dictNums[candidate] != i:
            min_index = str(min(i, dictNums[candidate]))
            max_index = str(max(i, dictNums[candidate]))
            combinations.add((f"{min_index},{max_index}"))

    result = []
    for combination in combinations:
        indexes = combination.split(",")
        first = int(indexes[0])
        second = int(indexes[1])
        result.append((first, second))

    return result if len(result) else None


nums = [1, 3, 5, 7, 9, 6]
# nums = []
target = 12
response = findTwoSum(nums, target)
print(response)
