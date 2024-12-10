"""Balanced Brackets
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""

# Not fast enough
def isBalancedOne(s) -> str:
    leftBrackets = []
    rightBracket = []

    for bracket in s:

        if bracket in "({[":
            leftBrackets.append(bracket)
        else:
            openBracket = leftBrackets.pop()
            combination = openBracket + bracket

            if combination not in ("()", "{}", "[]"):
                return "NO"

    return "NO" if leftBrackets or rightBracket else "YES"


def isBalanced(s) -> str:
    bracketValues = {
        "(": 1,
        ")": -1,
        "[": 2,
        "]": -2,
        "{": 3,
        "}": -3,
    }

    sum = 0

    for bracket in s:
        sum += bracketValues[bracket]

    return "NO" if sum else "YES"


s = "{[()]()]}"
print(isBalanced(s))
