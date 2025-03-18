"""
Given head, the head of a linked list, determine if the
linked list has a cycle in it.

If the linkedList has a cycle, return the position where
it has the cycle

If the linkedlist does not have a cycle, return -1
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = dict()
        currPosition = 0
        curr = head

        while curr:
            if curr in visited:
                return visited[curr]

            else:
                visited[curr] = currPosition

            curr = curr.next
            currPosition += 1

        return -1


solution = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node4

res1 = solution.hasCycle(node1)
print("res1", res1)
