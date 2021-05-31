# BinaryTree
import queue

# Nodo de un árbol binario
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Arbol Binario
class BinaryTree:
    def __init__(self):
        self.root = None

    # Recorrido pre order (para almacenar un árbol)
    def preOrder(self, TreeNode):

        if TreeNode != None:
            print(TreeNode.data, end=" ")
            self.preOrder(TreeNode.left)
            self.preOrder(TreeNode.right)

    # Recorrido in order (menor-mayor)
    def inOrder(self, TreeNode):

        if TreeNode != None:
            self.inOrder(TreeNode.left)
            print(TreeNode.data, end=" ")
            self.inOrder(TreeNode.right)

    # Recorrido post order (para liberar arbol)
    def postOrder(self, TreeNode):

        if TreeNode != None:
            self.postOrder(TreeNode.left)
            self.postOrder(TreeNode.right)
            print(TreeNode.data, end=" ")

    # Imprime el árbol nivel por nivel
    def levelByLevel(self, TreeNode):

        q = queue.Queue(100)
        q.put(self.root)

        while not q.empty():

            curr = q.get()

            if curr.left != None:
                q.put(curr.left)

            if curr.right != None:
                q.put(curr.right)

            print(curr.data, end=" ")

    # Imprimer el arbol binario dado un parámetro
    def printBinaryTree(self, option):

        if option == 1:  # PreOrder
            self.preOrder(self.root)

        elif option == 2:  # InOrder
            self.inOrder(self.root)

        elif option == 3:  # PostOrder
            self.postOrder(self.root)

        elif option == 4:  # Nivel por nivel
            self.levelByLevel(self.root)

        print()

    # Añade un nodo al árbol
    def add(self, TreeNode):

        if self.root == None:
            self.root = TreeNode

        else:

            curr = self.root
            flag = False

            while not flag:

                # El numero ya se encuentra en el árbol
                if curr.data == TreeNode.data:
                    flag = True

                # El nodo actual es menor que el del Nodo dado
                elif curr.data < TreeNode.data:

                    if curr.right != None:
                        curr = curr.right

                    else:
                        curr.right = TreeNode
                        flag = True

                # El nodo actual es mayor que el del Nodo dado
                else:

                    if curr.left != None:
                        curr = curr.left

                    else:
                        curr.left = TreeNode
                        flag = True

    # Regresa el numero más pequeño del árbol
    def getSmallest(self):

        curr = self.root

        if curr == None:
            return

        while curr.left != None:
            curr = curr.left

        return curr.data

    # Regresa el numero más grande del árbol
    def getBiggest(self):

        curr = self.root

        if curr == None:
            return

        while curr.right != None:
            curr = curr.right

        return curr.data


myBinaryTree = BinaryTree()
myBinaryTree.add(TreeNode(5))
myBinaryTree.add(TreeNode(2))
myBinaryTree.add(TreeNode(7))
myBinaryTree.add(TreeNode(1))
myBinaryTree.add(TreeNode(8))
myBinaryTree.add(TreeNode(9))

myBinaryTree.printBinaryTree(4)

# myBinaryTree.printBinaryTree(3)
# print(myBinaryTree.getBiggest())
