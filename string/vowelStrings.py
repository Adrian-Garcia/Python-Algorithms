"""2559. Count Vowel Strings in Ranges
https://leetcode.com/problems/count-vowel-strings-in-ranges/description/

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in
the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith
query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
    Output: [2,3,0]
    
    Explanation:
        The strings starting and ending with a vowel are "aba", "ece", "aa", "e".
        The answer to the query [0,2] is 2 (strings "aba" and "ece").
        to query [1,4] is 3 (strings "ece", "aa", "e").
        to query [1,1] is 0.
        We return [2,3,0].

Example 2:
    Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
    Output: [3,2,1]
    Explanation: Every string satisfies the conditions, so we return [3,2,1].

Constraints:
    1 <= words.length <= 105
    1 <= words[i].length <= 40
    words[i] consists only of lowercase English letters.
    sum(words[i].length) <= 3 * 105
    1 <= queries.length <= 105
    0 <= li <= ri < words.length
"""

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        Fastes solution O(n). Using Dynamic programming strategy, we create a
        prefix table to know how many vocal words have been accumulated.

        Example:
            Given this set of words, we can determine which elements are "vowel
            words":

                   yes      yes       no       no         yes
                ["apple", "orange", "grape", "banana", "avocado"]

            and with it, we create an array as prefix table to know the cumlative
            value of the words. (we always add a 0 at the beginning)

                [0,    1,       2,        2,       2,         3]
                [   "apple", "orange", "grape", "banana", "avocado"]

            for each query, we solve bu sibstracting positions:
                prefixSumArray[end + 1] - prefixSumArray[start]
        """

        vowels = set(["a", "e", "i", "o", "u"])
        prefixSumArray = [0]
        response = []
        count = 0

        for word in words:
            wordLen = len(word)
            if word[0] in vowels and word[wordLen - 1] in vowels:
                count += 1
            prefixSumArray.append(count)

        print("prefixSumArray", prefixSumArray)

        for query in queries:
            start = query[0]
            end = query[1]

            response.append(prefixSumArray[end + 1] - prefixSumArray[start])

        return response

    def vowelStringsAlsoTooSlow(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        # Basic iterative. Correct but too slow O(n2)
        vowels = set(["a", "e", "i", "o", "u"])
        newWords = []
        response = []

        for word in words:
            wordLen = len(word)
            newWords.append(
                True if word[0] in vowels and word[wordLen - 1] in vowels else False
            )

        for query in queries:
            start = query[0]
            end = query[1]
            wordsInRange = newWords[start : end + 1]

            counter = 0

            for word in wordsInRange:
                if word:
                    counter += 1

            response.append(counter)

        return response

    def vowelStringsTooSlow(
        self, words: List[str], queries: List[List[int]]
    ) -> List[int]:
        # Basic iterative. Correct but too slow O(n2)

        vowels = set(["a", "e", "i", "o", "u"])
        response = []

        for query in queries:
            start = query[0]
            end = query[1]
            wordsInRange = words[start : end + 1]

            counter = 0

            for word in wordsInRange:
                wordLen = len(word)

                if word[0] in vowels and word[wordLen - 1] in vowels:
                    counter += 1

            response.append(counter)

        return response


words1 = ["aba", "bcb", "ece", "aa", "e"]
queries1 = [[0, 2], [1, 4], [1, 1]]
solution1 = Solution().vowelStrings(words1, queries1)
print(solution1)

words2 = ["a", "e", "i"]
queries2 = [[0, 2], [0, 1], [2, 2]]
solution2 = Solution().vowelStrings(words2, queries2)
print(solution2)

words3 = ["apple", "orange", "grape", "banana", "avocado"]
queries3 = [[0, 2], [1, 3], [2, 4]]
solution3 = Solution().vowelStrings(words3, queries3)
print(solution3)
