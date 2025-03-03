'''Clone a Binary Tree
Given a binary tree, return a copy of it.

Input:
    Root of a binary tree

Output:
    Root of the copied binary tree
'''

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Solution():
    def preOrder(root):
        if root:
            print(root.info, end=" ")
            Solution.preOrder(root.left)
            Solution.preOrder(root.right)

    def inOrder(root):
        if root:
            Solution.inOrder(root.left)
            print(root.info, end=" ")
            Solution.inOrder(root.right)

    def postOrder(root):
        if root:
            Solution.postOrder(root.left)
            Solution.postOrder(root.right)
            print(root.info, end=" ")

    def __preOrderCopy(self, curr, copyNode):
        if not curr:
            return

        if curr.left != None:
            copyNode.left = Node(curr.left.info)

        if curr.right:
            copyNode.right = Node(curr.right.info)
        
        self.__preOrderCopy(curr.left, copyNode.left)
        self.__preOrderCopy(curr.right, copyNode.right)

    def cloneTree(self, root):
        if not root:
            return

        newHead = Node(root.info)

        self.__preOrderCopy(root, newHead)

        return newHead


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

newHead = Solution().cloneTree(node1)

print("Original")
print("PreOrder: ", end="")
Solution.preOrder(node1)
print("\nInOrder: ", end="")
Solution.inOrder(node1)
print("\nPostOrder: ", end="")
Solution.postOrder(node1)

print("\n\nCopy")
print("PreOrder: ", end="")
Solution.preOrder(newHead)
print("\nInOrder: ", end="")
Solution.inOrder(newHead)
print("\nPostOrder: ", end="")
Solution.postOrder(newHead)