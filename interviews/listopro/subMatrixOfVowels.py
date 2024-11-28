"""
You are given an n x m matrix.

Your job is ot find if there is a sub-matrix of 2x2 that contains all vowels

example_one = [
  ['aabbb'],
  ['aabbb'],
  ['bbbbb'],
]
result = 0-0


example_two = [
  ['abcde'],
  ['fghij'],
  ['klmno'],
]
result = not found
"""


def allVowelsInSubStrArr(subStrArr):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    for i in range(len(subStrArr)):
        for j in range(len(subStrArr[i])):
            if subStrArr[i][j] not in vowels:
                return False

    return True


def MatrixChallenge(strArr):
    for i in range(len(strArr)):
        for j in range(len(strArr[i])):

            if i + 1 < len(strArr) and j + 1 < len(strArr[i]):
                subStrArr = [
                    [strArr[i][j], strArr[i][j + 1]],
                    [strArr[i + 1][j], strArr[i + 1][j + 1]],
                ]

                if allVowelsInSubStrArr(subStrArr):
                    return str(i) + "-" + str(j)

    return "not found"


# keep this function call here
print(MatrixChallenge(input()))
