"""Balanced Brackets
https://www.hackerrank.com/challenges/balanced-brackets/problem
"""

# Not fast enough
def isBalanced(s) -> str:
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


s = "{[()]()]}"
print(isBalanced(s))
