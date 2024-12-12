"""Binary Search Tree : Insertion
https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
"""


class Node:
    def __init__(self, info, left=None, right=None, level=None):
        self.info = info
        self.left = left
        self.right = right
        self.level = level


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def preOrder(curr):
        if curr == None:
            return
        print(curr.info, end=" ")
        BinarySearchTree.preOrder(curr.left)
        BinarySearchTree.preOrder(curr.right)

    def levelByLevel(self):
        if not self.root:
            return

        queue = [self.root]

        while queue:
            curr = queue.pop(0)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            print(curr.info, end=" ")

    def insert(self, val):
        curr = self.root
        father = None

        while curr:

            if curr.info == val:
                return

            father = curr
            curr = curr.left if curr.info > val else curr.right

        if not father:
            return

        newNode = Node(val)

        if father.info > val:
            father.left = newNode
        else:
            father.right = newNode

        return self.root


bst = BinarySearchTree()
bst.root = Node(4)
bst.root.left = Node(2)
bst.root.right = Node(7)
bst.root.left.left = Node(1)
bst.root.left.right = Node(3)

# bst.levelByLevel()
BinarySearchTree.preOrder(bst.root)
print()

bst.insert(6)

# bst.levelByLevel()
BinarySearchTree.preOrder(bst.root)
print()
