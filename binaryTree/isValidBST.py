"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false   
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from typing import Optional
from sys import maxsize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTreeNodeDoesNotWork(
        self, curr: Optional[TreeNode], visited: set, prev: int
    ) -> bool:
        """
        This function does not work because it can not check wether a leaf node that is at the
        bottom of the tree is smaller than a father leaf.

        See [5,4,6,null,null,3,7] tree for more context
        """
        if curr == None:
            return True

        currVal = curr.val
        leftTreeNode = curr.left
        rightTreeNode = curr.right

        leftResult = self.checkTreeNodeDoesNotWork(leftTreeNode, visited, prev)

        if leftTreeNode != None and leftTreeNode.val > currVal:
            return False

        if rightTreeNode != None and rightTreeNode.val < currVal:
            return False

        if currVal in visited:
            return False
        visited.add(currVal)

        if currVal <= prev:
            return False
        prev = currVal

        if leftResult:
            return self.checkTreeNodeDoesNotWork(rightTreeNode, visited, prev)

        return False

    def isValidBSTDoesNotWork(self, root):
        visited = set()
        prev = -maxsize
        return self.checkTreeNodeDoesNotWork(root, visited, prev)

    def checkTreeNode(self, root):
        stack = []
        curr = root
        prev = -maxsize

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left

            elif stack:
                curr = stack.pop()
                currVal = curr.val

                if currVal <= prev:
                    return False
                prev = currVal

                curr = curr.right

            else:
                break

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkTreeNode(root)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().isValidBST(root))
