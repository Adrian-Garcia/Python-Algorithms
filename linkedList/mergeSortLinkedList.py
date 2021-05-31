class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def sortedMerge(self, leftList, rightList):
        result = None

        if leftList == None:
            return rightList

        if rightList == None:
            return leftList

        if leftList.data <= rightList.data:
            result = leftList
            result.next = self.sortedMerge(leftList.next, rightList)

        else:
            result = rightList
            result.next = self.sortedMerge(leftList, rightList.next)

        return result

    def mergeSort(self, head):

        if head == None or head.next == None:
            return head

        middle = self.getMiddle(head)
        headSecondList = middle.next

        middle.next = None

        leftList = self.mergeSort(head)
        rightList = self.mergeSort(headSecondList)

        sortedlist = self.sortedMerge(leftList, rightList)
        return sortedlist

    def getMiddle(self, head):

        if head == None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def __init__(self):
        self.head = None

    def append(self, val):

        newNode = ListNode(val)

        if self.head is None:
            self.head = newNode
            return
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = newNode


def printList(head):

    if head is None:
        print(" ")
        return

    curr_node = head

    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next

    print(" ")


myList = LinkedList()

myList.append(15)
myList.append(10)
myList.append(5)
myList.append(20)
myList.append(3)
myList.append(2)

myList.head = myList.mergeSort(myList.head)
printList(myList.head)
