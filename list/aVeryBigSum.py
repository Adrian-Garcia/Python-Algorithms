"""A Very Big Sum
https://www.hackerrank.com/challenges/a-very-big-sum/problem
"""


def aVeryBigSum(ar):
    response = 0

    for element in ar:
        response += element

    return response


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))
