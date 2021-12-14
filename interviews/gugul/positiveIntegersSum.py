"""
Given an integer N, you are asked to divide N into a sum of a maximal number of positive even integers. All the numbers should also be different.

For example, for N = 12, the following splits are valid: (2 + 10), (2 + 4 + 6) and (4 + 8). Among them, (2 + 4 + 6) contains the maximal number of integers. Note that N cannot be split into (2 + 2 + 4 + 4) as all the numbers should be different.

Write a function:

class Solution { public int[] solution(int N); }

which, given a positive integer number N, returns an array containing the numbers from any maximal possible answer (any valid combination may be returned). If N cannot be divided in such a way, return an empty array.

Result array should be returned as an array of integers.

Examples:

1. Given N = 6, your function should return [2, 4] or [4, 2].

2. Given N = 7, your function should return [] (an empty array) as there is no valid split.

3. Given N = 22, your function should return [2, 4, 6, 10] in any order.

4. Given N = 4, your function should return [4].

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000,000].
"""
import sys
from itertools import combinations


def get_positive_numbers(num):
    nums = []
    for i in range(num):
        n = (i + 1) * 2
        if n > num:
            return nums
        nums.append(n)

    return nums


def get_all_combinations(positiveNumbers):
    return sum(
        [
            list(map(list, combinations(positiveNumbers, i)))
            for i in range(len(positiveNumbers) + 1)
        ],
        [],
    )


def get_sum_target(combinations, target):
    response = []
    for comb in combinations:
        if sum(comb) == target:
            response.append(comb)

    return response


def solution(N):
    if N % 2 != 0:
        return []

    positiveNumbers = get_positive_numbers(N)
    combinations = get_all_combinations(positiveNumbers)
    subsets = get_sum_target(combinations, N)
    return max(subsets, key=len)


print(solution(10))
