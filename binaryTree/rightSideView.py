"""199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=problem-list-v2&envId=binary-tree

Given the root of a binary tree, imagine yourself standing on the right
side of it, return the values of the nodes you can see ordered from top
to bottom.

 Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]

Example 2:
    Input: root = [1,2,3,4,null,null,null,5]
    Output: [1,3,4,5]

Example 3:
    Input: root = [1,null,3]
    Output: [1,3]

Example 4:
    Input: root = []
    Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __preOrder(
        self, curr: TreeNode, rightSideView: List[int], currLevel: int
    ) -> None:
        if not curr:
            return

        if len(rightSideView) <= currLevel:
            rightSideView.append(curr.val)

        self.__preOrder(curr.right, rightSideView, currLevel + 1)
        self.__preOrder(curr.left, rightSideView, currLevel + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []
        self.__preOrder(root, rightSideView, 0)
        return rightSideView


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

print(Solution().rightSideView(root))
