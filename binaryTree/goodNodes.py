"""
Count Good Nodes in Binary Tree
Within a binary tree, a node x is considered good if the path from the
root of the tree to the node x contains no nodes with a value greater
than the value of node x

Given the root of a binary tree root, return the number of good nodes
within the tree.

Example 1:
    Input: root = [2,1,1,3,null,1,5]
    Output: 3

Example 2:
    Input: root = [1,2,-1,3,4]
    Output: 4

Constraints:
    1 <= number of nodes in the tree <= 100
    -100 <= Node.val <= 100
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __preOrder(
        self, curr: TreeNode, latestGoodNode: int, countGoodNodes: List[int]
    ) -> None:
        if not curr:
            return

        if curr.val >= latestGoodNode:
            latestGoodNode = curr.val
            countGoodNodes[0] += 1

        self.__preOrder(curr.left, latestGoodNode, countGoodNodes)
        self.__preOrder(curr.right, latestGoodNode, countGoodNodes)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        countGoodNodes = [0]
        self.__preOrder(root, root.val - 1, countGoodNodes)

        return countGoodNodes[0]


solution = Solution()

node1 = TreeNode(1)
node2 = TreeNode(2)
nodeN1 = TreeNode(-1)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = nodeN1

node2.left = node3
node2.right = node4

res1 = solution.goodNodes(node1)
print("res1", res1)

node3a = TreeNode(3)
node3b = TreeNode(3)
node4 = TreeNode(4)
node2 = TreeNode(2)

node3a.left = node3b

node3b.left = node4
node3b.right = node2

res2 = solution.goodNodes(node3a)
print("res2", res2)

node1 = TreeNode(1)
node2 = TreeNode(2)
nodeN1 = TreeNode(-1)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = nodeN1

node2.left = node3
node2.right = node4

res3 = solution.goodNodes(node1)
print("res3", res3)
