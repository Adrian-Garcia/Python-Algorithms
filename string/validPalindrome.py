'''
125. Valid Palindrome
	Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
	Note: For the purpose of this problem, we define empty string as valid palindrome.

	Example 1:
		Input: "A man, a plan, a canal: Panama"
		Output: true

	Example 2:
		Input: "race a car"
		Output: false

	Constraints:
		s consists only of printable ASCII characters.
'''

class Solution(object):
	def isPalindrome(self, s):

		validString = ""

		for char in s:
			if char.isalnum():
				validString += char.lower()

		reversedString = validString[::-1]
		return True if reversedString == validString else False

sol = Solution()

if sol.isPalindrome("0p"):
	print("Ajua")
else:
	print("Chale")