"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
"""


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeTwoLists(list1, list2) -> ListNode:
    head = ListNode(None)
    curr = head

    while list1 != None and list2 != None:
        val = None

        if list1.data < list2.data:
            val = list1.data
            list1 = list1.next

        else:
            val = list2.data
            list2 = list2.next

        curr.next = ListNode(val)
        curr = curr.next

    while list1 != None:
        curr.next = ListNode(list1.data)
        list1 = list1.next
        curr = curr.next

    while list2 != None:
        curr.next = ListNode(list2.data)
        list2 = list2.next
        curr = curr.next

    return head.next


def printList(head):
    curr = head

    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


list1node1 = ListNode(1)
list1node2 = ListNode(2)
list1node3 = ListNode(4)

list2node1 = ListNode(1)
list2node2 = ListNode(3)
list2node3 = ListNode(4)

list1node1.next = list1node2
list1node2.next = list1node3

list2node1.next = list2node2
list2node2.next = list2node3

h = mergeTwoLists(list1node1, list2node1)
printList(h)
