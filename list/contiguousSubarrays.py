"""Contiguous Subarrays
https://www.metacareers.com/profile/coding_practice_question/?problem_id=226517205173943&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122

You are given an array arr of N integers. For each index i, you are
required to determine the number of contiguous subarrays that fulfill
the following conditions:

    - The value at index i must be the maximum element in the
    contiguous subarrays, and
    - These contiguous subarrays must either start from or end on
    index i.

Signature
    int[] countSubarrays(int[] arr)

Input
    - Array arr is a non-empty list of unique integers that range
    between 1 to 1,000,000,000
    
    - Size N is between 1 and 1,000,000

Output
    An array where each index i contains an integer denoting the
    maximum number of contiguous subarrays of arr[i]
    
Example:
    arr = [3, 4, 1, 6, 2]
    output = [1, 3, 1, 5, 1]

    Explanation:
    
        For index 0 - [3] is the only contiguous subarray that starts
        (or ends) at index 0 with the maximum value in the subarray being 3.
        
        For index 1 - [4], [3, 4], [4, 1]
        
        For index 2 - [1]
        
        For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
        
        For index 4 - [2]
        
        So, the answer for the above input is [1, 3, 1, 5, 1]
"""

from typing import List


def countValidSubArrays(subArrs: List[List[int]], number: int) -> int:
    count = 1

    for subArr in subArrs:
        if max(subArr) == number:
            count += 1

    return count


def count_subarrays(arr) -> List[int]:
    response = []

    for i in range(len(arr)):

        start = i - 1
        end = i + 2
        subArrs = []

        while start >= 0 or end <= len(arr):
            if start >= 0:
                subArrs.append(arr[start : i + 1])

            if end <= len(arr):
                subArrs.append(arr[i:end])

            start -= 1
            end += 1

        response.append(countValidSubArrays(subArrs, arr[i]))

    return response


arr1 = [3, 4, 1, 6, 2]
arr2 = [2, 4, 7, 1, 5, 3]
print(count_subarrays(arr2))
