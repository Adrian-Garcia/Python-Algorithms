"""Arrays: Left Rotation
https://www.hackerrank.com/challenges/ctci-array-left-rotation/proble
"""


def rotLeft(a, d):
    dFixed = d % len(a)
    return a[dFixed:] + a[0:dFixed]


a = [1, 2, 3, 4, 5]
d = 6
print(rotLeft(a, d))
