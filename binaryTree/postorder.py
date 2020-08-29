class Node: 
	  
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def iterativePostorder(root):

	if root is None:
		return

	stack = []
	result = []

	stack.append(root)

	while stack:
		
		currNode = stack.pop()
		result.append(currNode)

		if currNode.left:
			stack.append(currNode.left)

		if currNode.right:
			stack.append(currNode.right)

	while result:
		currNode = result.pop()
		print(currNode.data, end=' ')

def recursivePostorder(root):
	if root is not None:
		recursivePostorder(root.left)
		recursivePostorder(root.right)
		print(root.data, end=' ')

root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 

print("--------Postorder------")

print("Iterative: ", end='')
iterativePostorder(root)
print ("\nRecursive: ", end='')
recursivePostorder(root)
print()