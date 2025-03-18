"""
2095. Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return
the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the
start using 0-based indexing, where ⌊x⌋ denotes the largest integer less
than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2,
respectively.
 
Example 1:
    Input: head = [1,3,4,7,1,2,6]
    Output: [1,3,4,1,2,6]

    Explanation:
        The above figure represents the given linked list. The indices of
        the nodes are written below.
        
        Since n = 7, node 3 with value 7 is the middle node, which is
        marked in red.
        
        We return the new list after removing this node. 

Example 2:
    Input: head = [1,2,3,4]
    Output: [1,2,4]

Example 3:
    Input: head = [2,1]
    Output: [2] 

Constraints:
    The number of nodes in the list is in the range [1, 105].
    1 <= Node.val <= 105
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        herr = head
        prev = None
        tortoise = head

        while herr and herr.next:
            prev = tortoise
            tortoise = tortoise.next
            herr = herr.next.next

        if prev != None:
            prev.next = prev.next.next
        else:
            head = None

        return head

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
solution.deleteMiddle(node1)
solution.printList(node1)
