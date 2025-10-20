"""
Reorder Linked List
https://neetcode.io/problems/reorder-linked-list

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example,
can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the
following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n
the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but
instead you must reorder the nodes themselves.

Example 1:
    Input: head = [2,4,6,8]
    Output: [2,8,4,6]

Example 2:
    Input: head = [2,4,6,8,10]
    Output: [2,10,4,8,6]

Constraints:
    1 <= Length of the list <= 1000.
    1 <= Node.val <= 1000
"""

from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        dq = deque()
        curr = head

        while curr:
            dq.append(curr)
            curr = curr.next

        prev = dq.popleft()
        currNum = 1

        while len(dq):
            curr = dq.pop() if currNum % 2 else dq.popleft()
            prev.next = curr
            prev = curr
            currNum += 1

        prev.next = None

    def printList(self, head) -> None:
        curr = head
        while curr:
            print(f"{curr.val} -> ", end="")
            curr = curr.next
        print(f"None")


solution = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


solution.printList(node1)
solution.reorderList(node1)
solution.printList(node1)
