class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None


def preOrder(curr, currHeight, maxHeight):
    if not curr:
        return

    currMaxHeight = maxHeight.pop()
    maxHeight.append(max(currHeight, currMaxHeight))
    preOrder(curr.left, currHeight + 1, maxHeight)
    preOrder(curr.right, currHeight + 1, maxHeight)


def height(root):
    if not root:
        return 0
    maxHeight = [0]
    preOrder(root, 1, maxHeight)
    return maxHeight.pop() - 1


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.right.left = Node(3)
root.right.left.right = Node(4)

print(height(root))
