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
    result = set()

    for i in range(len(nums)):
        num = nums[i]
        candidate = target - num

        if candidate in dictNums:
            if dictNums[candidate] == i:
                continue

            list_to_append = (
                str(max(i, dictNums[candidate]))
                + ","
                + str(min(i, dictNums[candidate]))
            )
            result.add(list_to_append)

    if not result:
        return None

    combinations = []
    for combination in result:
        first = int(combination.split(",")[0])
        second = int(combination.split(",")[1])
        combinations.append((first, second))

    return combinations


nums = [1, 3, 5, 7, 9, 6]
target = 12
response = findTwoSum(nums, target)
print(response)
