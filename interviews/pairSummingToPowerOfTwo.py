import math


def Log2(x):
    if x == 0:
        return False

    return math.log10(x) / math.log10(2)


def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))


def pairSummingToPowerOfTwo(a):
    dic = {}

    for i, v in enumerate(a):
        for j in range(i, len(a)):
            aux = a[i] + a[j]

            if aux not in dic:
                dic[aux] = 0

        dic[aux] += 1

    result = 0

    for x in dic:
        if x > 0:
            if isPowerOfTwo(x):
                result += dic[x]

    return result
