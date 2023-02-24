"""
Given an array of integers nums and an integer k, return the number of unique
k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are
true:

|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

A unique pair is defined as having two numbers such that these two numbers are
not seen in any other pair. For example, (1, 3) and (3, 1) are not unique
pairs, but (1, 3) and (2, 1) are.

Example 1:
  Input: nums = [3,1,4,1,5], k = 2
  Output: 2
  Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
  Although we have two 1s in the input, we should only return the number of
  unique pairs.

Example 2:
  Input: nums = [1,2,3,4,5], k = 1
  Output: 4
  Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3),
  (3, 4) and (4, 5).
"""


def foo(nums, k):
    set_nums = set(nums)
    result = set()

    for num in nums:
        candidate = num - k

        if candidate in set_nums:
            new_pair = str(sorted([num, candidate]))
            result.add(new_pair)

    return len(result)


nums = [3, 1, 4, 1, 5]
k = 2

print(foo(nums, k))
