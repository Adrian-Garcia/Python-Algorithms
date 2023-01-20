import heapq


def minimizeCost(arr):
    totalCostOperation = 0
    heapq.heapify(arr)

    while len(arr) > 1:
        one = heapq.heappop(arr)
        two = heapq.heappop(arr)

        currCost = one + two
        totalCostOperation += currCost
        arr.append(currCost)

    return totalCostOperation


res = minimizeCost([25, 10, 20])
print(res)
