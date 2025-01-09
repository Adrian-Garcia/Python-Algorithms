"""
• You are given a binary search tree. Goal is to find sum of all elements in the tree which are in range [low, high].
• Input: binary search tree, and range [low, high]


Get sum of all elements in binary search tree which are in range [low, high] inclusive.
        6

     4     8

   3   5 7   9

 2

        6

     4     8

   3   6 7   9

 2


         3.5
        [2,3,4,5]
// Input: [2, 5] => 14
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#                             6     2    5    4
def preOrderCodedOnInterview(curr, min, max, sum):
    if not curr:
        return sum

    if min <= curr.val <= max:
        return (
            sum
            + curr.val
            + preOrderCodedOnInterview(curr.left, min, max, sum)
            + preOrderCodedOnInterview(curr.right, min, max, sum)
        )

    if min <= curr.val:
        preOrderCodedOnInterview(curr.left, min, max, sum)

    if max >= curr.val:
        preOrderCodedOnInterview(curr.right, min, max, sum)

    return sum


def sumOfRangeCodedOnInterview(root, range):
    min, max = range[0], range[1]
    sum = 0

    return preOrderCodedOnInterview(root, min, max, sum)


def preOrder(curr, min, max, sum):
    if not curr:
        return

    if min <= curr.val <= max:
        sum[0] += curr.val

        preOrder(curr.left, min, max, sum)
        preOrder(curr.right, min, max, sum)
        return

    if min <= curr.val:
        preOrder(curr.left, min, max, sum)

    if max >= curr.val:
        preOrder(curr.right, min, max, sum)

    return sum


def sumOfRange(root, range):
    min, max = range[0], range[1]
    sum = [0]

    preOrder(root, min, max, sum)

    return sum.pop()


node6 = TreeNode(6)
node4 = TreeNode(4)
node8 = TreeNode(8)
node3 = TreeNode(3)
node5 = TreeNode(5)
node7 = TreeNode(7)
node9 = TreeNode(9)
node2 = TreeNode(2)

node6.left = node4
node6.right = node8
node4.left = node3
node4.right = node5
node8.left = node7
node8.right = node9
node3.left = node2

result = sumOfRange(node6, [2, 5])
print("result", result)
