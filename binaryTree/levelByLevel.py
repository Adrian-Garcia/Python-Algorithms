class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelByLevel(root: TreeNode):
    queue = []
    queue.append(root)

    while queue:
        curr = queue.pop(0)

        if curr.left != None:
            queue.append(curr.left)

        if curr.right != None:
            queue.append(curr.right)

        print(curr.data, end=" ")


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

levelByLevel(root)
