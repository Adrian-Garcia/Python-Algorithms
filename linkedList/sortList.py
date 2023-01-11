"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Example 3:
    Input: head = []
    Output: []

Constraints:
    - The number of nodes in the list is in the range [0, 5 * 104].
    - -105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
(i.e. constant space)?
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeSort(self, listNodes: List[Optional[ListNode]]):
        if len(listNodes) <= 1:
            return

        mid = len(listNodes) // 2
        listLeft = listNodes[:mid]
        listRight = listNodes[mid:]

        self.mergeSort(listLeft)
        self.mergeSort(listRight)

        listNodeIndex = 0
        listLeftIndex = 0
        listRightIndex = 0

        while listLeftIndex < len(listLeft) and listRightIndex < len(listRight):

            if listLeft[listLeftIndex].val < listRight[listRightIndex].val:
                listNodes[listNodeIndex] = listLeft[listLeftIndex]
                listLeftIndex += 1

            else:
                listNodes[listNodeIndex] = listRight[listRightIndex]
                listRightIndex += 1

            listNodeIndex += 1

        while listLeftIndex < len(listLeft):
            listNodes[listNodeIndex] = listLeft[listLeftIndex]
            listLeftIndex += 1
            listNodeIndex += 1

        while listRightIndex < len(listRight):
            listNodes[listNodeIndex] = listRight[listRightIndex]
            listRightIndex += 1
            listNodeIndex += 1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        listNodes = []

        while curr:
            listNodes.append(curr)
            curr = curr.next

        self.mergeSort(listNodes)

        head = ListNode(None)
        curr = head

        for listNode in listNodes:
            curr.next = listNode
            curr = curr.next

        curr.next = None

        return head.next


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)

curr = Solution().sortList(head)
while curr:
    print(curr.val, end=" ")
    curr = curr.next
