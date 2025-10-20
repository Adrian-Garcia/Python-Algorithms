class Solution:
    def __getLongestPalindrome(self, s, low, top, longestString, longestLen):
        while low >= 0 and top < len(s) and s[low] == s[top]:
            currLen = top - low + 1

            if currLen > longestLen:
                longestString = s[low : top + 1]
                longestLen = currLen

            low -= 1
            top += 1

        return longestString, longestLen

    def longestPalindrome(self, s: str) -> str:
        longestString = ""
        longestLen = 0

        for i in range(len(s)):

            # Odd case
            longestString, longestLen = self.__getLongestPalindrome(
                s, i, i, longestString, longestLen
            )

            # Even case
            longestString, longestLen = self.__getLongestPalindrome(
                s, i, i + 1, longestString, longestLen
            )

        return longestString


solution = Solution()
s1 = "abadb"
res1 = solution.longestPalindrome(s1)
print("res1", res1)
