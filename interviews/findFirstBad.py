'''
Description
Given an (expensive) API "bool isBadRevision(int revision)" write a functions that returns first bad revision in the range

Question Statement
Consider a version control system, and a series of sequential code revisions that could be either "good" or "bad". If a revision is bad, all subsequent revisions are also bad. Suppose you have an API that tells you if a particular revision is bad. Write a function that returns first bad revision in a given range of revisions. [Assume valid input.]

1 -> good
2 -> good
200 -> good
.....
500 -> bad
501 -> bad

API :   isBadRevision (int) -> true if bad, false if good (expensive)

Write
int findFirstBad (int firstGood, int lastBad)
'''
def isBadRevision(revision):
    return revision < 3

def findFirstBad(firstGood, lastBad):
    start = firstGood
    last = lastBad

    lastBad = start

    while (last > start):

        middle = int((start + last) / 2)

        if (isBadRevision(middle)):
            last = middle
            lastBad = middle
        
        else:
            start = middle

    return lastBad

print(findFirstBad(1,5))