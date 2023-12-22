"""
Given a number (n), determine if there exists a number k between 1 and n such that the sum of the numbers to the left of (k)
is equal to the sum of the numbers to its right (i.e. the sum of the numbers between 1 and k-1 is equal to the sum of 
the numbers between k+1 and n). If such number exists, return it, otherwise, return -1.

Example:

n: 8 --> Input
k: 6 --> Output

1 2 3 4 5 [6] 7 8

1+2+3+4+5 = 15
7+8 = 15

Example 2:

n: 9 --> Input
k: -1 --> Output

left = additionFormula(5) = ?
right = additionFormula(9) - additionFormula)(6)

           
1 2 3 4 5 [6] 7 8 9

1 100 = 101
2 99 = 101

101 * N / 2

n*(n+1)/2
5 * 5 + 1


0 -> -1
1 -> 1
"""

"""
Example:

n: 8 --> Input
k: 6 --> Output


left < right


          X     
1 2 3 4 5 6 7 8

maxAdditionalFormula

maxAdditionalFormula = 36
left = 15
right = 36 - 21 = 15
"""


def additionFormula(n: int) -> int:
    # 6 * 7 // 2 = 21
    return n * (n + 1) // 2


def validNumber(n: int) -> bool:
    return not (n < 0 and type(n) != int)


def getKNumber(n: int) -> int:
    if not validNumber(n):
        return -2

    maxAdditionalFormula = additionFormula(n)

    for i in range(n):
        currentNumber = i + 1
        left = additionFormula(currentNumber - 1)
        right = maxAdditionalFormula - additionFormula(currentNumber)

        if left == right:
            return currentNumber

    return -1
