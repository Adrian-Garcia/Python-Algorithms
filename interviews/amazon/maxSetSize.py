import math


def getConcurrencies(riceBags):
    concurrencies = {}

    for riceBag in riceBags:
        sqrt = math.sqrt(riceBag)
        if not (isinstance(sqrt, int) and int(sqrt) in riceBags):
            concurrencies[riceBag] = []

    return concurrencies


def getMaxSize(riceBags, concurrencies):
    maxSize = -1
    for factor in concurrencies:
        currentFactor = factor
        while currentFactor in riceBags:
            concurrencies[factor].append(currentFactor)
            currentFactor *= currentFactor

        maxSize = max(maxSize, len(concurrencies[factor]))

    return maxSize


def maxSetSize(riceBags):
    riceBags = set(riceBags)
    concurrencies = getConcurrencies(riceBags)
    maxSize = getMaxSize(riceBags, concurrencies)

    if maxSize > 1:
        return maxSize

    return -1


print(maxSetSize([3, 9, 4, 2, 16]))
