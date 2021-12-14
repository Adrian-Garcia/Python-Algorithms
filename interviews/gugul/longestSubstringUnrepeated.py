"""
You are given a string S consisting of N lowercase letters of the English alphabet. Find the length of the longest substring of S in which the number of occurrences of each letter is equal.

For example, given S = "ababbcbc", substrings in which every letter occurs the same number of times are: "a", "b", "c", "ab", "ba", "bb", "bc", "cb", "abab" and "bcbc". The longest among them are "abab" and "bcbc" and their length equals 4.

Write a function:

int solution(string &S);

that, given the string S of length N, returns the length of the longest substring in which the number of occurrences of each letter is equal.

Examples:
Given S = "ababbcbc", the function should return 4, as explained above.
Given S = "aabcde", the function should return 5. The longest substring is "abcde", in which all letters occur once.
Given S = "aaaa", the function should return 4. The longest substring is "aaaa", in which all letters occur four times.
Given S = "daababbd", the function should return 6. The longest substring is "aababb", in which all letters occur three times.
Assume that:
N is an integer within the range [1..80];
string S consists only of lowercase letters (a-z).
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

"""
import sys


def get_substrings_from_string(string):
    return [
        string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)
    ]


def get_even_repeat(substr):
    chars = {}
    flag = -1

    for char in substr:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for char in chars:
        if flag == -1:
            flag = chars[char]

        if chars[char] != flag:
            return -1

    return len(substr)


def get_longest_unreapeated(substrings):
    longest = -1
    for substr in substrings:
        unrepeated = get_even_repeat(substr)
        if unrepeated > longest:
            longest = unrepeated

    return longest


def solution(S):
    if S == "":
        return 0

    substrings = get_substrings_from_string(S)
    return get_longest_unreapeated(substrings)


s = "pleasehireme"
print(solution(s))
