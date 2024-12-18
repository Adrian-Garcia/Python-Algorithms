""" Reverse to Make Equal
https://www.metacareers.com/profile/coding_practice_question/?problem_id=2869293499822992&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122

Given two arrays A and B of length N, determine if there is a way to make A
equal to B by reversing any subarrays from array B any number of times.

Signature
    bool areTheyEqual(int[] arr_a, int[] arr_b)

Input
    All integers in array are in the range [0, 1,000,000,000].

Output
    Return true if B can be made equal to A, return false otherwise.

Example
    A = [1, 2, 3, 4]
    B = [1, 4, 3, 2]
    output = true

After reversing the subarray of B from indices 1 to 3, array B will equal array A.
"""


def are_they_equal(array_a, array_b):
    if len(array_a) != len(array_b):
        return False

    if array_a == array_b:
        return True

    i = 0
    start = []
    subArrB = []
    currArr = []

    for i in range(len(array_a)):
        if array_a[i] != array_b[i] and not start:
            start = array_a[:i]
            subArrB.append(array_a[i])
            continue

        if start:
            subArrB.append(array_a[i])
            currArr = start + subArrB + array_b[i + 1 :]
            """
            print("array_a", array_a)
            print("array_b", array_b)
            print("start  ", start)
            print("subArrB", subArrB)
            print("currArr", currArr)
            print()
            """
            if currArr == array_a:
                return True

    return currArr == array_a


array_a = [1, 2, 3, 4]
array_b = [1, 2, 3, 5]

print(are_they_equal(array_a, array_b))
