"""
Lowest Common Ancestor in Binary Search Tree
https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree

Given a binary search tree (BST) where all node values are unique, and two
nodes from the tree p and q, return the lowest common ancestor (LCA) of the
two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a
tree T such that both p and q as descendants. The ancestor is allowed to be
a descendant of itself.

Example 1:
    Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
    Output: 5

Example 2:
    Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
    Output: 3

    Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a
    descendant of itself.

Constraints:
    2 <= The number of nodes in the tree <= 100.
    -100 <= Node.val <= 100
    p != q
    p and q will both exist in the BST.
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    solutionAncestors = []

    def __getAncestors(
        self,
        curr: TreeNode,
        target: TreeNode,
        ancestors: List[TreeNode],
        response: List[TreeNode],
    ) -> None:
        if response != [] or curr == None:
            return

        ancestors.append(curr)

        if curr.val == target.val:
            response = ancestors
            Solution.solutionAncestors = ancestors

            return

        self.__getAncestors(curr.left, target, ancestors.copy(), response)
        self.__getAncestors(curr.right, target, ancestors.copy(), response)

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        pAncestors = []
        qAncestors = []

        self.__getAncestors(root, q, [], qAncestors)
        qAncestors = Solution.solutionAncestors
        Solution.solutionAncestors = []

        self.__getAncestors(root, p, [], pAncestors)
        pAncestors = Solution.solutionAncestors

        latestAncestor = pAncestors[0]

        while pAncestors and qAncestors:
            pAncestor = pAncestors.pop(0)
            qAncestor = qAncestors.pop(0)

            if pAncestor != qAncestor:
                return latestAncestor

            latestAncestor = pAncestor

        return latestAncestor


solution = Solution()

node5 = TreeNode(5)
node3 = TreeNode(3)
node8 = TreeNode(8)
node1 = TreeNode(1)
node4 = TreeNode(4)
node7 = TreeNode(7)
node9 = TreeNode(9)
node2 = TreeNode(2)

node5.left = node3
node5.right = node8

node3.left = node1
node3.right = node4

node8.left = node7
node8.right = node9

node1.right = node2

res1 = solution.lowestCommonAncestor(node5, node3, node8)
print("res1", res1.val)

res2 = solution.lowestCommonAncestor(node5, node3, node4)
print("res2", res2.val)
