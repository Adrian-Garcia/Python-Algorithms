"""Ice Cream Parlor
https://www.hackerrank.com/challenges/icecream-parlor/problem
"""


def iceCreamParlor(m, arr):
    visited = dict()

    for i in range(len(arr)):
        neededNum = m - arr[i]

        if neededNum in visited:
            return [visited[neededNum] + 1, i + 1]

        visited[arr[i]] = i

    return -1


m = 3
arr = [1, 1, 2, 3]

print(iceCreamParlor(m, arr))
