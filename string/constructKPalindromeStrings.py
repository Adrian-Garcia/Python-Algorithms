'''
1400. Construct K Palindrome Strings
	Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
	Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

Example 1:
	Input: s = "annabelle", k = 2
	Output: true
	Explanation: You can construct two palindromes using all characters in s.
	Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
	Input: s = "leetcode", k = 3
	Output: false
	Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
	Input: s = "true", k = 4
	Output: true
	Explanation: The only possible solution is to put each character in a separate string.

Example 4:
	Input: s = "yzyzyzyzyzyzyzy", k = 2
	Output: true
	Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.

Example 5:
	Input: s = "cr", k = 7
	Output: false
	Explanation: We don't have enough characters in s to construct 7 palindromes.

Constraints:
	1 <= s.length <= 10^5
	All characters in s are lower-case English letters.
	1 <= k <= 10^5
'''

class Solution(object):

	def __splitStr(self, s):
		
		deconstructedStr = {}

		for char in s:
			if char in deconstructedStr:
				deconstructedStr[char] = deconstructedStr[char] + 1

			else:
				deconstructedStr[char] = 1

		return deconstructedStr

	def __getNumOfInpairs(self, deconstructedStr):

		numberOfInpairs = 0

		for char in deconstructedStr:
			if deconstructedStr[char] % 2:
				numberOfInpairs += 1

		if numberOfInpairs == 0:
			numberOfInpairs = 1

		return numberOfInpairs

	def canConstruct(self, s, k):

		deconstructedStr = self.__splitStr(s)

		minPalindrome = self.__getNumOfInpairs(deconstructedStr)
		maxPalindrome = len(s)

		return (k >= minPalindrome and k <= maxPalindrome)

sol = Solution()

print(sol.canConstruct("annabelle", 2))