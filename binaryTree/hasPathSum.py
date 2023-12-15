"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.

Example 3:
    Input: root = [], targetSum = 0
    Output: false
    Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __preOrder(self, node, sum, targetSum):
        newSum = sum + node.val

        if not node.right and not node.left:
            return newSum == targetSum

        leftResult = (
            self.__preOrder(node.left, newSum, targetSum) if node.left else False
        )
        rightResult = (
            self.__preOrder(node.right, newSum, targetSum) if node.right else False
        )

        return leftResult or rightResult

    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        return self.__preOrder(root, 0, targetSum)


solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)

print(solution.hasPathSum(root, 1))
