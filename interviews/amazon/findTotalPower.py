def powerFunction(combination):
    return


def findTotalPower1(power):
    result = 0
    for i in range(len(power)):
        for j in range(i, len(power)):
            combination = power[i : j + 1]
            result += min(combination) * sum(combination)

    return result % (10**9 + 7)


# print(findTotalPower([2,3,2,1]))

import heapq


def getPrefix(prefix, i, j):
    return prefix[j] - prefix[i]


def getResult(power, last, currSum, preSum, prefix):
    result = 0
    for i in range(len(power)):
        x = power[i]
        currCount = 0
        poppedSum = 0
        poppedPreSum = 0
        sumOne = 0

        while last:
            a, b, c, d = heapq.heappop(last)
            a = -a

            if a >= x:
                y = b + getPrefix(prefix, d, i - 1) * c
                poppedSum += y
                poppedPreSum += y * a
                currCount += c
                sumOne += a * c

            else:
                heapq.heappush(last, (-a, b, c, d))
                break

        lastSum = currSum - sumOne
        poppedSum += power[i] * (currCount + 1)
        result += poppedSum * power[i] + lastSum * power[i] + preSum - poppedPreSum
        currSum = lastSum + (currCount + 1) * power[i]
        preSum = poppedSum * power[i] + lastSum * power[i] + preSum - poppedPreSum
        heapq.heappush(last, (-power[i], poppedSum, currCount + 1, i))

    return result


def findTotalPower(power):
    mod = 10**9 + 7
    prefix = [power[i] for i in range(len(power))]

    for i in range(1, len(power)):
        prefix[i] += prefix[i - 1]

    return getResult(power, [], 0, 0, prefix) % mod


print(findTotalPower([2, 3, 2, 1]))
