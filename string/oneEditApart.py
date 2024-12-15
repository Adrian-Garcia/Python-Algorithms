"""Question 3: Edit Distance
https://www.facebook.com/careers/life/sample_interview_questions

Write a function that returns whether two words are exactly "one edit" away using the following signature:
    bool OneEditApart(string s1, string s2);

An edit is:
    - Inserting one character anywhere in the word (including at the beginning and end)
    - Removing one character
    - Replacing one character

Examples:
    OneEditApart("cat", "dog") = false
    OneEditApart("cat", "cats") = true
    OneEditApart("cat", "cut") = true
    OneEditApart("cat", "cast") = true
    OneEditApart("cat", "at") = true
    OneEditApart("cat", "act") = false
"""
from typing import List


def getMaxAndMinStrings(s1: str, s2: str) -> List[str]:
    if len(s1) > len(s2):
        return s1, s2
    return s2, s1


def oneEditApart(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) >= 2:
        return False

    maxS, minS = getMaxAndMinStrings(s1, s2)
    differences = 0
    i = 0

    while differences < 2 and i < len(maxS) and i < len(minS):

        if maxS[i] == minS[i]:
            i += 1

        else:
            if len(maxS) == len(minS):
                minS = minS.replace(minS[i], maxS[i], 1)

            else:
                minS = minS[:i] + maxS[i] + minS[i:]

            differences += 1
            i = 0

        print()

    return differences < 2


print(oneEditApart("cat", "act"))
