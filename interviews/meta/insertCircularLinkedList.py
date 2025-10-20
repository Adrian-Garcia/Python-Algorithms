"""
You are given a sorted circular linked list of integers.
Write a method that, given a pointer to a node and an integer, inserts a new node with that integer in the correct position and returns the newly inserted node.

Example:
    2>4>6(6>>2). insert(2*, 5) ---> 2>4>5>6(6>>2)
"""

"""
Notes

1 -> 2 -> 4
     <-

3

     p         n
1 -> 2 -> 3 -> 4
     <-

3

p    n
1 -> 2
  <- 

prev = head
next = head.next
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def insert(listNode: ListNode, number):
    prev = listNode
    next = listNode.next

    biggest = None

    """
    number = 2
    prev = 3
    next = 4
    biggest = None
    listNode = 1*

         p    n
    1 -> 3 -> 4

    """

    while True:
        if prev.val <= number <= next.val:
            newNode = ListNode(number)
            prev.next = newNode
            newNode.next = next
            return newNode

        if prev.val > next.val:
            biggest = prev

        if prev == biggest:
            newNode = ListNode(number)
            biggest.next = newNode
            newNode.next = listNode
            return newNode

        prev = prev.next
        next = next.next
