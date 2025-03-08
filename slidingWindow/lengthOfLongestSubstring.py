"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "zxyzxyz"
    Output: 3
    Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
    Input: s = "xxxx"
    Output: 1

Constraints:
    0 <= s.length <= 1000
    s may consist of printable ASCII characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l = 0
        r = 1

        maxSubStr = 0
        currSubString = s[l:r]
        lettersInSubString = set(currSubString)

        while r < len(s):
            newChar = s[r]

            if newChar in lettersInSubString:
                while s[l] != newChar:
                    l += 1
                l += 1

            currSubString = s[l : r + 1]
            maxSubStr = max(maxSubStr, len(currSubString))
            lettersInSubString = set(currSubString)
            r += 1

        return maxSubStr


solution = Solution()

s1 = "abcabcbb"
res1 = solution.lengthOfLongestSubstring(s1)
print("res1", res1)


s2 = "zxyzxyz"
res2 = solution.lengthOfLongestSubstring(s2)
print("res2", res2)

s3 = "xxxx"
res3 = solution.lengthOfLongestSubstring(s3)
print("res3", res3)
