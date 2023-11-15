"""
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []
 
Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return root

        queue = [root]

        while queue:
            curr_node = queue.pop(0)

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            curr_node.left, curr_node.right = curr_node.right, curr_node.left

        return root


solution = Solution()

tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)

res_root = solution.invertTree(tree)
print(res_root.data, res_root.left.data, res_root.right.data)
