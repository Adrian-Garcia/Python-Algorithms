""" 141.Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
 
Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Simple set solution. Fast but uses linear memory. Beats 79.38% in runtime but only 7.69% in memory
        """
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return True

            visited.add(curr)
            curr = curr.next

        return False

    def hasCycleHareTortoise(self, head: ListNode) -> bool:
        """
        Hare-Tortoise algorithm

        Uses constant memory and has linear time complexity but fails in this case:

        Input
            head = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
            pos = 24

        Output
            false

        Expected
            true
        """
        tortoise = head
        hare = head
        start = True

        if not head or not head.next:
            return False

        while tortoise and hare:
            if tortoise == hare and not start:
                return True

            hare = hare.next.next if hare.next and hare.next.next else None
            tortoise = tortoise.next
            start = False

        return False


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
