


firstBad =  2
                    1           5
def findFirstBad(firstGood, lastBad):
    
    start = firstGood # 2
    last = lastBad    # 2
    
    lastBad = start
    
    #   .
    # 1 2 3 4 5
    while (last > start):
    
        middle = (start + last) / 2 

        if (isBadRevision(middle)):
            last = middle
            lastBad = middle
        
        else:
            start = middle

    return lastBad

My internet connection failed :(
    
    
    
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
Example 1:

[8,3,1]
[8,3,6,4]
[8,3,6,7]
[8,10,14,13]    

8
n2


                                  8
                        3                    10
                  1         6                       14
                        4       7             13
Input: [8,3,10,1,6,null,14,null,null,4,7,13] 
Output: 7 
Explanation:  We have various ancestor-node differences, some of which are given below : |8 - 3| = 5 |3 - 7| = 4 |8 - 1| = 7 |10 - 13| = 3 Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Note:
The number of nodes in the tree is between 2 and 5000.

Each node will have value between 0 and 100000.
    
[8,3,1]

    
    
import math
biggestDifference = math.MIN_INT

def getBiggestDifference(treePath):
    
    biggest = math.MIN_INT
    
    for i in treePath:
        for j in treePath:
            difference = abs(i - j)
    
            if (difference > biggest):
                biggest = difference
    
    return biggest

    
# 
def countDifferences(r, biggestDifference, treePath)

    if (r.left == None and r.right == None):
        potencialDifference = getBiggestDifference(treePath)
        if potencialDifference > biggestDifference:
            biggestDifference = potencialDifference
    
    else:
        treePath.append(r.val)
    
    if(r.left != None):
        countDifferences(r.left, biggestDifference, treePath)
    
    if(r.right != None):
        countDifferences(r.right, biggestDifference, treePath)
    
    
def ancestorDifference(root):

    countDifferences(root, biggestDifference, [])
    
    return biggestDifference    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    