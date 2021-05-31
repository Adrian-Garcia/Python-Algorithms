# Linked List

# Nodo de una lista
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Lista Encadenada
class LinkedList:
    def __init__(self):
        self.head = None

    # Aniade un nodo en la primera posicion
    def addFirst(self, ListNode):

        if self.head == None:
            self.head = ListNode

        else:
            aux = self.head
            self.head = ListNode
            self.head.next = aux

    # Aniade un nodo en cierta posicion
    def addAt(self, ListNode, index):

        if index == 0:
            self.addFirst(ListNode)

        else:

            curr = self.head
            i = 0

            while curr != None:

                if i == index - 1:

                    aux = curr.next
                    curr.next = ListNode
                    curr.next.next = aux

                    break

                curr = curr.next
                i += 1

    # Aniade un nodo en la ultima posicion
    def addLast(self, ListNode):

        if self.head == None:
            self.head = ListNode

        else:

            curr = self.head

            while curr.next != None:
                curr = curr.next

            curr.next = ListNode

    # Elimina el primer nodo de la lista
    def deleteFirst(self):

        if self.head == None:
            return

        else:
            self.head = self.head.next

    # Elimina el ultimo nodo de la lista
    def deleteLast(self):

        if self.head == None:
            return

        elif self.head.next == None:
            self.head = None

        else:

            curr = self.head

            while curr.next.next != None:
                curr = curr.next
            curr.next = None

    # Elimina un nodo de la lista dada una posicion especifica
    def deleteAt(self, index):

        if index == 0:
            self.deleteFirst()

        else:

            curr = self.head
            i = 0

            while curr.next != None:

                if i == index - 1:
                    curr.next = curr.next.next
                    return

                curr = curr.next
                i += 1

    # Invierte el orden de la lista
    def reverse(self):

        if self.head == None or self.head.next == None:
            return

        else:

            prevNode = None
            currNode = self.head
            nextNode = self.head.next

            while nextNode != None:

                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode
                nextNode = nextNode.next

            currNode.next = prevNode
            self.head = currNode

    # Operator +=
    def __iadd__(self, other):

        Safe = self.head
        curr1 = self.head
        curr2 = other.head

        while curr1.next != None:
            curr1 = curr1.next

        while curr2 != None and curr1 != None:
            curr1.next = ListNode(curr2.data)
            curr1 = curr1.next
            curr2 = curr2.next

        curr1.next = None
        self.head = Safe

    # Imprime la lista completa
    def printList(self):

        curr = self.head

        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


# Listas
myLinkedList = LinkedList()
otherLinkedList = LinkedList()

myLinkedList.addLast(ListNode(1))
myLinkedList.addLast(ListNode(3))
myLinkedList.addFirst(ListNode(0))
myLinkedList.addAt(ListNode(2), 2)
myLinkedList.addAt(ListNode(-1), 0)
myLinkedList.addAt(ListNode(4), 5)
myLinkedList.printList()

otherLinkedList.addLast(ListNode(5))
otherLinkedList.addLast(ListNode(6))
otherLinkedList.addLast(ListNode(7))
otherLinkedList.addLast(ListNode(8))

# myLinkedList+=otherLinkedList
# myLinkedList.printList()

# myLinkedList.deleteFirst()
# myLinkedList.deleteLast()
# myLinkedList.deleteAt(3)
# myLinkedList.printList()

# myLinkedList.reverse()
# myLinkedList.printList()
