"""49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

 
Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Explanation:
        There is no string in strs that can be rearranged to form "bat".
        The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]] 

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

from typing import List


class Solution:
    def __getAnagrams(self, strs) -> dict:
        anagrams = dict()

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in anagrams:
                anagrams[sortedStr].append(s)
            else:
                anagrams[sortedStr] = [s]

        return anagrams

    def __groupAnagrams(self, anagrams) -> List[str]:
        result = []

        for anagram in anagrams:
            result.append(anagrams[anagram])

        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = self.__getAnagrams(strs)
        return self.__groupAnagrams(anagrams)


strs0 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs0))
