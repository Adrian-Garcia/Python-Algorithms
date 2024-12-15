"""Question 2: Look and Say
https://www.facebook.com/careers/life/sample_interview_questions

Implement a function that outputs the Look and Say sequence:
    1
    11
    21
    1211
    111221
    312211
    13112221
    1113213211
    31131211131221
    13211311123113112211

    one
    one 1 = 11
    two 1 = 21
    one 2, one 1 = 1211
    ...
"""


def generateNewLevel(prevLevel) -> str:
    newChar = prevLevel[0]
    newLevel = ""
    count = 0

    for i in range(len(prevLevel)):
        if newChar == prevLevel[i]:
            count += 1
        else:
            newLevel += str(count) + newChar
            count = 1
            newChar = prevLevel[i]

    newLevel += str(count) + newChar
    return newLevel


def lookAndSay(n: int):
    if n < 0:
        return

    prevLevel = "1"
    print(prevLevel)

    for _ in range(n - 1):
        prevLevel = generateNewLevel(prevLevel)
        print(prevLevel)


lookAndSay(10)
