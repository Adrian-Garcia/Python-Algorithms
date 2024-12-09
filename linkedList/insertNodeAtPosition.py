"""Insert a node at a specific position in a linked list
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
"""


class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insertNodeAtPosition(llist, data, position):
    curr = llist
    currPosition = 1

    while curr != None:

        if currPosition == position:
            newNext = curr.next
            newNode = SinglyLinkedListNode(data)
            curr.next = newNode
            newNode.next = newNext
            return llist

        curr = curr.next
        currPosition += 1


def printList(head):
    curr = head
    while curr:
        print(f"{curr.data} -> ", end="")
        curr = curr.next
    print("None")


node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)
node4 = SinglyLinkedListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

printList(node1)
node1 = insertNodeAtPosition(node1, 5, 2)
printList(node1)
