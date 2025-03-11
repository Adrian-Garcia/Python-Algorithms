"""
Kth Smallest Integer in BST
https://neetcode.io/problems/kth-smallest-integer-in-bst

Given the root of a binary search tree, and an integer k, return
the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less
than the node's key.

The right subtree of every node contains only nodes with keys
greater than the node's key.

Both the left and right subtrees are also binary search trees.

Example 1:
    Input: root = [2,1,3], k = 1
    Output: 1

Example 2:
    Input: root = [4,3,5,2,null], k = 4
    Output: 5

Constraints:
    1 <= k <= The number of nodes in the tree <= 1000.
    0 <= Node.val <= 1000
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __inOrderCount(
        self, curr: TreeNode, currCount: List[int], result: List[int], k: int
    ) -> None:
        if not curr or len(result):
            return

        self.__inOrderCount(curr.left, currCount, result, k)

        currCount[0] += 1

        if currCount[0] == k:
            result.append(curr.val)
            return

        self.__inOrderCount(curr.right, currCount, result, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        currCount = [0]
        result = []

        self.__inOrderCount(root, currCount, result, k)

        return result.pop()


solution = Solution()

node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node4.left = node3
node4.right = node5

node3.left = node2

res1 = solution.kthSmallest(node4, 1)
print("res1", res1)
