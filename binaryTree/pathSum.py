'''
Path Sum
	Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path 
	equals the given sum.

Note: 
	A leaf is a node with no children.

Example:

	Given the below binary tree and sum = 22,

	      5
	     / \
	    4   8
	   /   / \
	  11  13  4
	 /  \      \
	7    2      1

	return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
class TreeNode(object):

	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):

	def hasPathSum(self, root, sum):
		
		if (root == None):
			return False

		s = [root]

		while(s):
			
			curr = s.pop(-1)

			if(curr.left):
				curr.left.val += curr.val
				s.append(curr.left)
			
			if(curr.right):
				curr.right.val += curr.val
				s.append(curr.right)

			if(not curr.left and not curr.right and curr.val == sum):
				return True

		return False


sol = Solution()

nodeT0 = TreeNode()
nodeT1 = TreeNode()
nodeT2 = TreeNode()
nodeT3 = TreeNode()
nodeT4 = TreeNode()
nodeT5 = TreeNode()

nodeT0.val = 0
nodeT1.val = 1
nodeT2.val = 2
nodeT3.val = 3
nodeT4.val = 4
nodeT5.val = 5

nodeT0.left = nodeT1
nodeT0.right = nodeT2
nodeT1.left = nodeT3
nodeT2.left = nodeT4


print(sol.hasPathSum(nodeT0, 2))