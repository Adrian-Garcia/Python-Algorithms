"""
25. Reverse Nodes in k-Group
Hard
Given the head of a linked list, reverse the nodes of the list k at a time, and
return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end,
should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be
changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
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
    def __haveKGroup(self, head, k):
        count = 1
        curr = head

        while curr and count < k:
            count += 1
            curr = curr.next

        return curr if count == k else None

    def reverseKGroup(self, head, k):
        curr = head

        while self.__haveKGroup(curr, k):
            curr_k = curr
            nums = []

            for _ in range(k):
                nums.append(curr_k.val)
                curr_k = curr_k.next

            for _ in range(k):
                curr.val = nums.pop()
                curr = curr.next

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

head.printList()
solution.reverseKGroup(head, 2)
head.printList()
