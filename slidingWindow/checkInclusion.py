"""
Permutation in String (medium)
https://neetcode.io/problems/permutation-string

You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2, then
return true.

Both strings only contain lowercase letters.

Example 1:
    Input: s1 = "abc", s2 = "lecabee"
    Output: true
    Explanation: The substring "cab" is a permutation of "abc" and
    is present in "lecabee".

Example 2:
    Input: s1 = "abc", s2 = "lecaabee"
    Output: false

Constraints:
    1 <= s1.length, s2.length <= 1000
"""


class Solution:

    # Not finished
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = dict()
        s2Dict = dict()

        for c in s1:
            if c in s1Dict:
                s1Dict[c] += 1
            else:
                s1Dict[c] = 1

        for i in range(len(s1)):
            c = s2[i]
            if c in s2Dict:
                s2Dict[c] += 1
            else:
                s2Dict[c] = 1

        for i in range(len(s2) - len(s1)):
            if s1Dict == s2Dict:
                return True

        return False

    def checkInclusionN2(self, s1: str, s2: str) -> bool:
        sortedS1 = sorted(s1)

        for start in range(len(s2)):
            end = start + len(s1)

            if end > len(s2):
                break

            subStr = s2[start:end]
            sortedSubStr = sorted(subStr)

            if sortedS1 == sortedSubStr:
                return True

        return False


solution = Solution()

s1 = "abc"
s2 = "lecabee"
res1 = solution.checkInclusionN2(s1, s2)
print("res1", res1)


s1 = "abc"
s2 = "lecaabee"
res2 = solution.checkInclusion(s1, s2)
print("res2", res2)

s1 = "adc"
s2 = "dcda"
res3 = solution.checkInclusion(s1, s2)
print("res3", res3)
