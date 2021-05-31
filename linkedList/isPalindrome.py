"""
Palindrome Linked List
	Given a singly linked list, determine if it is a palindrome.

Example 1:
	Input: 1->2
	Output: false

Example 2:
	Input: 1->2->2->1
	Output: true

Follow up:
	Could you do it in O(n) time and O(1) space?
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getSize(self, head):

        curr = head
        size = 0

        while curr != None:
            size += 1
            curr = curr.next

        return size

    def isPalindrome(self, head):

        if head == None:
            return head

        size = self.getSize(head)
        path = int(size / 2)

        prevNode = None
        currNode = head
        nextNode = head.next

        for i in range(path - 1):
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next

        currNode.next = prevNode

        self.printList(currNode)
        self.printList(nextNode)

    def printList(self, head):

        while head != None:
            print("{} -> ".format(head.val), end="")
            head = head.next
        print()


sol = Solution()
node0 = ListNode()
node1 = ListNode()
node2 = ListNode()
node3 = ListNode()

node0.val = 0
node1.val = 1
node2.val = 2
node3.val = 3
node3.val = 4

node0.next = node1
node1.next = node2
node2.next = node3

print(sol.isPalindrome(node0))
