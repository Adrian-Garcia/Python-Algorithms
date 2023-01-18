def getRangeThatAllFiltersOverlap(filterRanges):
    minRange = float("-inf")
    maxRange = float("inf")

    for i in range(len(filterRanges)):
        minRange = max(minRange, filterRanges[i][0])

    for i in range(len(filterRanges)):
        maxRange = min(maxRange, filterRanges[i][1])

    return minRange, maxRange


def countSignals(frequencies, filterRanges):
    signalCounter = 0
    minRange, maxRange = getRangeThatAllFiltersOverlap(filterRanges)

    for frequency in frequencies:
        if minRange <= frequency <= maxRange:
            signalCounter += 1

    return signalCounter


frequencies = [20, 5, 6, 7, 12]
filterRanges = [[10, 20], [5, 15], [5, 30]]

res = countSignals(frequencies, filterRanges)
print(res)
