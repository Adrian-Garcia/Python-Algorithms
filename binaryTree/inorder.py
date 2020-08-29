class Node: 

	# Constructor to create a new node
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def iterativeInorder(root):

	currNode = root
	stack = []

	while True:

		if currNode is not None:
			stack.append(currNode)
			currNode = currNode.left


		elif(stack):
			currNode = stack.pop()
			print(currNode.data, end=' ')
			currNode = currNode.right

		else:
			break

def recursiveInorder(root):
	if root is not None:
		recursiveInorder(root.left)
		print(root.data, end=' ')
		recursiveInorder(root.right)

root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 

print("--------Inorder--------")

print("Iterative: ", end='')
iterativeInorder(root)

print("\nRecursive: ", end='')
recursiveInorder(root)

print()