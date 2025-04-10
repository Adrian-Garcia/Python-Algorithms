""" Not finished
Remove Node From End of Linked List
https://neetcode.io/problems/remove-node-from-end-of-linked-list

You are given the beginning of a linked list head, and an
integer n.

Remove the nth node from the end of the list and return the
beginning of the list.

Example 1:
    Input: head = [1,2,3,4], n = 2
    Output: [1,2,4]

Example 2:
    Input: head = [5], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 2
    Output: [2]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        prev = None
        curr = head
        position = size - (n % size) if size != n else 1
        counter = 0

        print("n            ", n)
        print("size         ", size)
        print("position     ", position)

        if size <= 1:
            return None

        if position == 1:
            head = head.next
            return head

        while counter < position:
            prev = curr
            curr = curr.next
            counter += 1

        prev.next = prev.next.next
        return head

    def printList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr:
            print(f"{curr.val} -> ", end="")
            curr = curr.next
        print("None")


solution = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

# solution.printList(node1)
# res1 = solution.removeNthFromEnd(node1, 5)
# solution.printList(res1)

# node5 = ListNode(5)

# solution.printList(node5)
# res2 = solution.removeNthFromEnd(node5, 1)
# solution.printList(res2)

node1 = ListNode(1)
node1.next = ListNode(2)

solution.printList(node1)
res3 = solution.removeNthFromEnd(node1, 2)
solution.printList(res3)
