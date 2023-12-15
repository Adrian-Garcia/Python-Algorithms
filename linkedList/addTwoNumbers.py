"""
2. Add Two Numbers
Medium
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
 

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
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
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        prev = None
        curr = head
        reminder = 0

        while l1 and l2:
            curr_num = l1.val + l2.val + reminder
            reminder = 1 if curr_num >= 10 else 0
            curr.val = curr_num % 10

            prev = curr
            curr.next = ListNode()
            curr = curr.next
            l2 = l2.next
            l1 = l1.next

        while l1:
            curr_num = l1.val + reminder
            reminder = 1 if curr_num >= 10 else 0
            curr.val = curr_num % 10

            prev = curr
            curr.next = ListNode()
            curr = curr.next
            l1 = l1.next

        while l2:
            curr_num = l2.val + reminder
            reminder = 1 if curr_num >= 10 else 0
            curr.val = curr_num % 10

            prev = curr
            curr.next = ListNode()
            curr = curr.next
            l2 = l2.next

        if reminder:
            curr.val = 1
        else:
            prev.next = None

        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l1.printList()
l2.printList()

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
l3.printList()
