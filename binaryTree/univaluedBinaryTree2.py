"""
Univalued Binary Tree
	A binary tree is univalued if every node in the tree has the same value.
	Return true if and only if the given tree is univalued.

Example 1:
	Input: [1,1,1,1,1,null,1]
	Output: true

Example 2:
	Input: [2,2,2,5,2]
	Output: false

Note:
	The number of nodes in the given tree will be in the range [1, 100].
	Each node's value will be an integer in the range [0, 99].
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isUnivalTree(self, root):
        def check(r, val):

            if r is None:
                return True

            if r.val == val:
                return check(r.left, val) and check(r.right, val)

            return False

        return check(root, root.val)


sol = Solution()

nodeT0 = TreeNode()
nodeT1 = TreeNode()
nodeT2 = TreeNode()

nodeT0.val = 1
nodeT1.val = 1
nodeT2.val = 2

nodeT0.left = nodeT1
nodeT0.right = nodeT2

print(sol.isUnivalTree(nodeT0))
