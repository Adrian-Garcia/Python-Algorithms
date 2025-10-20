# TODO: Not sure if works. Please check when possible

"""

                    e
1 -> 3 -> 4 -> 5 -> 2



"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printListNodes(head):
        curr = head

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        next = head.next
        end = None
        size = 0
        count = 0

        while curr:
            size += 1
            end = curr
            curr = curr.next

        curr = head

        # print("curr", curr)
        # print("next", next)
        # print("count", count)
        # print("size", size)

        while curr and next and count < size // 2:
            ListNode.printListNodes(head)
            print("curr", curr.val)
            print("next", next.val)
            print()

            curr.next = curr.next.next
            end.next = next
            end = next
            end.next = None
            curr = curr.next
            next = curr.next
            count += 1

        return head

    def oddEvenListLolNope(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        curr = head
        even = head.val % 2 == 0
        lastValid = None

        while curr:
            if (even and curr.val % 2 == 0) or (not even and curr.val % 2 == 1):
                lastValid = curr
            curr = curr.next

        print("lastValid", lastValid.val)
        print("even", even)
        print()

        currLast = lastValid
        curr = head
        prev = head

        while curr != lastValid and curr and curr.next:
            print("curr.val", curr.val)
            ListNode.printListNodes(head)

            if not ((even and curr.val % 2 == 0) or (not even and curr.val % 2 == 1)):
                # print("lastValid", lastValid)

                newNode = ListNode(curr.val)
                newNode.next = currLast.next
                currLast.next = newNode
                currLast = newNode

                print("currLast.val", currLast.val)

                curr.val = curr.next.val
                curr.next = curr.next.next




            curr = curr.next

            
            print()

        return head

    def oddEvenListWrongApproach(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        curr = head
        prev = head
        queue = []

        while curr:
            if curr.val % 2 == 0:
                queue.append(curr.val)
                curr.val = curr.next.val
                curr.next = curr.next.next

            prev = curr
            curr = curr.next

        curr = prev

        while len(queue):
            currVal = queue.pop(0)
            curr.next = ListNode(currVal)
            curr = curr.next

        return head
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# ListNode.printListNodes(node1)
# node1 = Solution().oddEvenList(node1)
# ListNode.printListNodes(node1)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node2.next = node1
node1.next = node3
node3.next = node5
node5.next = node6
node6.next = node4
node4.next = node7

# ListNode.printListNodes(node2)
# node2 = Solution().oddEvenList(node2)
# ListNode.printListNodes(node2)

node1 = ListNode(1)
node11 = ListNode(1)

node1.next = node11
ListNode.printListNodes(node1)
node1 = Solution().oddEvenList(node1)
ListNode.printListNodes(node1)
