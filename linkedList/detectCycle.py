"""142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/description/

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to (0-indexed). It is -1 if there is no cycle. Note that pos
is not passed as a parameter.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return

    def detectCycleHareTortoise(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Does not work"""
        tortoise = head
        hare = head
        start = True

        if not head or not head.next:
            return

        while tortoise and hare:
            if tortoise == hare and not start:
                return tortoise.next

            hare = hare.next.next if hare.next and hare.next.next else None
            tortoise = tortoise.next
            start = False

        return


nodeVal1 = ListNode(1)
nodeVal2 = ListNode(2)
nodeVal3 = ListNode(3)
nodeVal4 = ListNode(4)
nodeVal5 = ListNode(5)

nodeVal1.next = nodeVal2
nodeVal2.next = nodeVal3
nodeVal3.next = nodeVal4
nodeVal4.next = nodeVal5
nodeVal5.next = nodeVal2

print(Solution().hasCycle(nodeVal1))
