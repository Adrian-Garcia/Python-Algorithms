"""
Given the root of a binary tree containing integers, 
print each column from left to right, and within each
column print the values from top to bottom.


Input:
     6
    / \
   3   4
  /   / \
 5   1   0
  \     /
   2   8
  / \
 9   7

Output:
    5 9 3 2 6 1 7 4 8 0

"""


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class TreeNodeOrder:
    def __init__(self, val, leftLevel=None, topLevel=None) -> None:
        self.val = val
        self.leftLevel = leftLevel
        self.topLevel = topLevel

    def __lt__(self, other):
        print("self.val", self.val)
        print("other.val", other.val)
        print("self.leftLevel", self.leftLevel)
        print("self.leftLevel", other.leftLevel)
        print("self.topLevel", self.topLevel)
        print("self.topLevel", other.topLevel)

        if self.leftLevel < other.leftLevel:
            print("returned on 1")
            print()

            return True

        if self.topLevel < other.topLevel:
            print("returned on 2")
            print()

            return True

        print("returned on 3")
        print()
        return False


def preOrder(curr, listOfNodes, leftLevel, topLevel):
    if not curr:
        return

    listOfNodes.append(TreeNodeOrder(curr.val, leftLevel, topLevel))

    preOrder(curr.left, listOfNodes, leftLevel - 1, topLevel + 1)
    preOrder(curr.right, listOfNodes, leftLevel + 1, topLevel + 1)


def verticalTraversal(root):
    listOfNodes = []
    preOrder(root, listOfNodes, 0, 0)
    sortedNodes = sorted(listOfNodes)

    res = []

    for node in sortedNodes:
        res.append(node.val)

    return res


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# res1 = verticalTraversal(root)
# print("res1", res1)

"""

Input:
     6
    / \
   3   4
  /   / \
 5   1   0
  \     /
   2   8
  / \
 9   7

Output:
    5 9 3 2 6 1 7 4 8 0

"""


node6 = TreeNode(6)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1 = TreeNode(1)
node0 = TreeNode(0)
node2 = TreeNode(2)
node8 = TreeNode(8)
node9 = TreeNode(9)
node7 = TreeNode(7)

node6.left = node3
node6.right = node4

node3.left = node5

node4.left = node1
node4.right = node0

node0.left = node8

node5.right = node2

node2.left = node9
node2.right = node7


res2 = verticalTraversal(node6)
print("res2", res2)
