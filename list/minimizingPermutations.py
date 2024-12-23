"""Minimizing Permutations
https://www.metacareers.com/profile/coding_practice_question/?problem_id=292715105029046&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122

In this problem, you are given an integer N, and a permutation,
P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N).
You want to rearrange the elements of the permutation into
increasing order, repeatedly making the following operation:

Select a sub-portion of the permutation, (a_i, ..., a_j), and
reverse its order.

Your goal is to compute the minimum number of such operations
required to return the permutation to increasing order.

Signature
    int minOperations(int[] arr)

Input
    Array arr is a permutation of all integers from 1 to N, N
    is between 1 and 8

Output
    An integer denoting the minimum number of operations
    required to arrange the permutation in increasing order

Example
    If N = 3, and P = (3, 1, 2), we can do the following
    operations:
    
        1. Select (1, 2) and reverse it: P = (3, 2, 1).
        2. Select (3, 2, 1) and reverse it: P = (1, 2, 3).

    output = 2
"""


def minOperations(arr):
    indexDict = dict()
    count = 0

    for i in range(len(arr)):
        indexDict[arr[i]] = i

    for i in range(len(arr)):
        neededNumber = i + 1
        if arr[i] != neededNumber:
            neededIndex = indexDict[neededNumber]
            arr[i], arr[neededIndex] = arr[neededIndex], arr[i]
            count += 1

    return count


arr1 = [1, 2, 5, 4, 3]
arr2 = [3, 1, 2]

print(minOperations(arr1))
print(minOperations(arr2))
