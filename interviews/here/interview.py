"""
/**
Two strings are anagrams of each other if they contain the same characters, only the order of character in both the strings is different.
"coat" is an anagram of "taco". Both words have the exact same characters, only in different orders.
"coat" is not an angram of "code". They are having not the exact same characters.
**/

/**
2. Groups of anagrams:

Given a list of words, return a sequence of separate groups, where all words in that group are anagrams. For example, 
given:
  ["art", "sop", "ops", "art", "rat", "cheese"] 
output:
  [
    ["art", "tar", "rat"],
    ["ops", "sop"], 
    ["cheese"]
    ["value"]
  ]

The order of the output does not matter. 
**/

{
  3 = [art, tar, rat]
  2 =  ["ops", "sop"], 
  1 = [["cheese"], ["value"]]
}
"""


def anagrams(anagrams_list):

    copied_anagrams_list = anagrams_list.copy()
    anagram_dict = dict()  # string, [string]

    # anagrams_list = ["art", "ops", "ops", "art", "art", "cheees"]

    for anagram in anagrams_list:
        sort(anagram)

    for i in range(len(anagrams_list)):
        if anagram_list[i] in anagram_dict:
            anagram_dict[anagram_list[i]].append(copied_anagrams_list[i])
        else:
            anagram_dict[anagram_list[i]] = [copied_anagrams_list[i]]

    return [anagram_dict.values()]
