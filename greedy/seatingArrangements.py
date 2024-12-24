"""Seating Arrangements (Does not work)
https://www.metacareers.com/profile/coding_practice_question/?problem_id=2444722699191194&c=1261090001694699&psid=275492097255885&practice_plan=0&b=0111122
"""
import itertools


def minOverallAwkwardness(arr):
    arrPermutations = itertools.permutations(arr)
    minAkwardness = 999999999
    minPermutations = []
    maxAkwardness = -999999999

    for permutation in list(arrPermutations):
        currAkwardness = 0

        for i in range(len(permutation)):
            currPerson = permutation[i]
            nextPerson = (
                permutation[i + 1] if i + 1 < len(permutation) else permutation[0]
            )

            currAkwardness += abs(currPerson - nextPerson)

        if currAkwardness == minAkwardness:
            minPermutations = [permutation]

        if currAkwardness < minAkwardness:
            minPermutations = [permutation]
            minAkwardness = currAkwardness

    print("minPermutations", minPermutations)
    print("minAkwardness", minAkwardness)

    for permutation in list(minPermutations):
        currAkwardness = 0
        for i in range(len(permutation)):
            currPerson = permutation[i]
            nextPerson = (
                permutation[i + 1] if i + 1 < len(permutation) else permutation[0]
            )
            currAkwardness = abs(currPerson - nextPerson)
            maxAkwardness = max(maxAkwardness, currAkwardness)

    return maxAkwardness


def minOverallAwkwardness0(arr):
    """
    Did not understood this correctly. The correct method is the other
    """

    arrPermutations = itertools.permutations(arr)
    minAkwardness = 999999999

    for permutation in list(arrPermutations):
        currAkwardness = 0

        for i in range(len(permutation)):
            currPerson = permutation[i]
            nextPerson = (
                permutation[i + 1] if i + 1 < len(permutation) else permutation[0]
            )

            currAkwardness += abs(currPerson - nextPerson)

        minAkwardness = min(minAkwardness, currAkwardness)

    return minAkwardness


def minOverallAwkwardness1(arr):
    arrPermutations = itertools.permutations(arr)
    minAkwardness = 999999999
    maxAkwardness = -99999999
    minPermutations = []

    for permutation in list(arrPermutations):
        currAkwardness = 0

        for i in range(len(permutation)):
            currPerson = permutation[i]
            nextPerson = (
                permutation[i + 1] if i + 1 < len(permutation) else permutation[0]
            )

            currAkwardness += abs(currPerson - nextPerson)

        if currAkwardness == minAkwardness:
            minPermutations.append(permutation)

        if currAkwardness < minAkwardness:
            minAkwardness = currAkwardness
            minPermutations = [permutation]

    print("minPermutations", minPermutations)

    newMinAkwardness = 9999999
    for permutation in minPermutations:
        for i in range(len(permutation)):
            currPerson = permutation[i]
            nextPerson = (
                permutation[i + 1] if i + 1 < len(permutation) else permutation[0]
            )

            currAkwardness = abs(currPerson - nextPerson)

            maxAkwardness = max(maxAkwardness, currAkwardness)

        newMinAkwardness = min(newMinAkwardness, maxAkwardness)

    return newMinAkwardness


arr0 = [1, 2, 3]
arr1 = [5, 10, 6, 8]
arr2 = [1, 2, 5, 3, 7]

# print(minOverallAwkwardness1(arr0))
print(minOverallAwkwardness1(arr1))
# print(minOverallAwkwardness1(arr2))
