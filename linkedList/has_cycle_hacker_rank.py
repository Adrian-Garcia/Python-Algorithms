"""Cycle Detection
https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
"""


class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def has_cycle(head):
    if not head or not head.next:
        return 0

    hare = head.next
    tortoise = head

    while hare and tortoise:
        if hare == tortoise or hare.next == tortoise:
            return 1

        hare = hare.next.next if hare.next and hare.next.next else None
        tortoise = tortoise.next

    return 0


node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)
node4 = SinglyLinkedListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

print(has_cycle(node1))
