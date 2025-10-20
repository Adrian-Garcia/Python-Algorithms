""" Group Anagrams
https://neetcode.io/problems/anagram-groups

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
    Input: strs = ["act","pots","tops","cat","stop","hat"]
    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
    Input: strs = ["x"]
    Output: [["x"]]

Example 3:
    Input: strs = [""]
    Output: [[""]]

Constraints:
    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        strs =      ["act","pots","tops","cat","stop","hat"]
        orderStrs = {
            "act": ["act", "cat"],
            "opst": ["pots", "tops", "stop"],
            "aht": ["hat"]
        }
        """

        strsDict = dict()

        for word in strs:
            orderedWord = "".join(sorted(word))

            if orderedWord in strsDict:
                strsDict[orderedWord].append(word)

            else:
                strsDict[orderedWord] = [word]

        return strsDict.values()


strs = ["act", "pots", "tops", "cat", "stop", "hat"]

print(Solution().groupAnagrams(strs))
