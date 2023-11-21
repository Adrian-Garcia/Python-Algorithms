"""
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]
 
Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        curr = self
        while curr:
            print(curr.val, end=" -> ") if curr.next else print(curr.val, end="")
            curr = curr.next
        print("\n")


class Solution(object):
    def swapPairs(self, head):
        curr = head

        while curr:
            if curr.next:
                curr.val, curr.next.val = curr.next.val, curr.val
                curr = curr.next.next
            else:
                curr = None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

head.printList()
solution.swapPairs(head)
head.printList()
