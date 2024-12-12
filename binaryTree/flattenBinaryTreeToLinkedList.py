"""114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=binary-tree

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child
pointer points to the next node in the list and the left child pointer is
always null.

The "linked list" should be in the same order as a pre-order traversal of
the binary tree.
 

Example 1:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [0]
    Output: [0]

Constraints:
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __preOrder(self, curr: TreeNode, nodes: List[TreeNode]) -> None:
        if not curr:
            return

        nodes.append(curr)
        self.__preOrder(curr.left, nodes)
        self.__preOrder(curr.right, nodes)

    def __constructNewThree(self, nodes: List[TreeNode]) -> None:
        newRoot = nodes.pop(0)
        prev = newRoot
        newRoot.left = None

        while nodes:
            node = nodes.pop(0)
            prev.right = node
            prev.left = None
            prev = node

        return newRoot

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        nodes = []
        self.__preOrder(root, nodes)
        return self.__constructNewThree(nodes)
