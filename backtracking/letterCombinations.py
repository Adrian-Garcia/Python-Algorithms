"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    phone = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        digits_chars = []
        for digit in digits:
            digits_chars.append(Solution.phone[int(digit)])

        self.__addCombination(digits_chars, 0, "", result)

        return result

    def __addCombination(
        self, digits_chars, curr_index, curr_combination, result
    ) -> None:
        if curr_index >= len(digits_chars):
            return curr_combination

        curr_digit = digits_chars[curr_index]

        for char in curr_digit:
            next_combination = curr_combination + char
            curr_result = next_combination + self.__addCombination(
                digits_chars, curr_index + 1, next_combination, result
            )

            if len(curr_result) == len(digits_chars) * 2:
                result.append(curr_result[: len(digits_chars)])

        return ""


solution = Solution()

digits1 = "23"
res1 = solution.letterCombinations(digits1)
print("res1", res1)
