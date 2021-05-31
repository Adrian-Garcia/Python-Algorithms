class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterativePreorder(root):

    if root is None:
        return

    stack = []
    stack.append(root)

    while stack:

        currNode = stack.pop()
        print(currNode.data, end=" ")

        if currNode.right is not None:
            stack.append(currNode.right)
        if currNode.left is not None:
            stack.append(currNode.left)


def recursivePreorder(root):
    if root is not None:
        print(root.data, end=" ")
        recursivePreorder(root.left)
        recursivePreorder(root.right)


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print("--------Preorder-------")

print("Iterative: ", end="")
iterativePreorder(root)
print("\nRecursive: ", end="")
recursivePreorder(root)
print()
