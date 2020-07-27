'''
3. Longest Substring Without Repeating Characters
	Given a string, find the length of the longest substring without repeating characters.

Example 1:
	Input: "abcabcbb"
	Output: 3 
	Explanation: The answer is "abc", with the length of 3. 

Example 2:
	Input: "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.

Example 3:
	Input: "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# abccdefghij


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if s == '':
			return 0

		repeatedChars = set()
		longestSubStr = 0

		for currChar in s:
			if currChar in repeatedChars:
				sizeSubStr = len(repeatedChars)
				longestSubStr = sizeSubStr if sizeSubStr > longestSubStr else longestSubStr
				repeatedChars.clear()
				repeatedChars.add(currChar)

			else:
				repeatedChars.add(currChar)

		sizeSubStr = len(repeatedChars)
		longestSubStr = sizeSubStr if sizeSubStr > longestSubStr else longestSubStr
		return longestSubStr

sol = Solution()

print(sol.lengthOfLongestSubstring("dvdf"))