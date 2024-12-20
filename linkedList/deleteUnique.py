"""Delete unique nodes
Delete all the nodes that have a unique consecutive value.

Example 1:
    Input: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    Output: 1 -> 1 -> 4 -> 4
    Explanation: 2 and 3 appear only once consecutivelly. 1 and 4 appear twice

Example 2:
    Input: 1 -> 1 -> 2 -> 3 -> 2 -> 2
    Output: 1 -> 1 -> 2 -> 2
    Explanation: 2 and 3 appear only once consecutivelly. 1 and 2 appear twice

Example 3:
    Input: 1
    Output: None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(head: ListNode) -> None:
    curr = head
    while curr:
        print(curr.val, "-> ", end="")
        curr = curr.next
    print("None")


def deleteUnique(head: ListNode) -> ListNode:
    if not head or not head.next:
        return

    while head and head.next:
        if head.val == head.next.val:
            head = head.next
        else:
            break

    next = None
    curr = head
    lastDouble = None

    while curr and curr.next:
        next = curr.next

        if curr.val == next.val:
            lastDouble = curr.val

        if curr.val != next.val and lastDouble != curr.val:
            curr.val = next.val
            curr.next = curr.next.next
            continue

        curr = curr.next

    return head


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

printList(node1)
deleteUnique(node1)
printList(node1)
