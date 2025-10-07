"""
Add Binary
https://leetcode.com/problems/add-binary/description/

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
    - Each string consists only of '0' or '1' characters.
    - 1 <= a.length, b.length <= 10^4
    - Each string is either "0" or doesn't contain any leading zero.
"""


class Solution(object):
    def __addCol(self, aNum, bNum, remind, res):
        chars = aNum + bNum + remind
        chars_count = chars.count("1")

        if chars_count == 3:
            res += "1"
            remind = "1"

        elif chars_count == 2:
            res += "0"
            remind = "1"

        elif chars_count == 1:
            res += "1"
            remind = "0"

        else:
            res += "0"
            remind = "0"

        return remind

    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]

        res = []
        remind = "0"
        i = 0

        while i < len(a) and i < len(b):
            remind = self.__addCol(a[i], b[i], remind, res)
            i += 1

        while i < len(a):
            remind = self.__addCol(a[i], "0", remind, res)
            i += 1

        while i < len(b):
            remind = self.__addCol("0", b[i], remind, res)
            i += 1

        if remind == "1":
            res += "1"

        return "".join(res[::-1])

    def addBinaryBitOperation(self, a, b):
        aNum = int(a, 2)
        bNum = int(b, 2)

        resNum = aNum + bNum

        resNum = bin(resNum)
        return resNum.replace("0b", "")


sol = Solution()
res = sol.addBinary("1010", "1011")
print("res", res)
