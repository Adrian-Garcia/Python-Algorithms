# Amazon is working on a shipping optimization in which packages to be shipped to the same destination region could be grouped.

# Suppose that, in a fulfillment center, packages flow in a conveyor belt with a capacity of “k” packages; and there is an optical
# reader in the beginning of the conveyor belt reading each package’s destination region; it beeps whenever the current package’s
# destination region is the same of another package which is still in the conveyor belt.

# You were assigned to develop a service which will receive as input a stream of numbers corresponding to packages’ destination regions,
# as well as an integer “k” representing the conveyor belt’s capacity. The output of your service should be how many times the optical reader would beep.

# Example:
# - Input: Stream=[1, 2, 3, 4, 2, 1, 1, 2, 4], k=3
# - Output: 2, 1, 2   beeps->3
# next, hasNext


class List:
    val: int
    next: List


#
"""                             c
Stream = [1, 2, 3, 4, 2, 1, 1, 2, 4], k=3
conveyorBelt = [1, 1, 2]
result = [2, 1, 2]
currVal = 2
"""

#
# [1, 1, 5, 7]

# n log n
def conveyorBelt(stream, k):

    curr = stream
    orderConveyorBelt = orderedSet()
    conveyorBelt = []

    result = []

    while curr.hasNext:
        currVal = curr.next

        # log n
        if currVal in orderConveyorBelt:
            result.append(currVal)

        if len(conveyorBelt) >= k:
            orderedConveyorBelt.remove(conveyorBelt.pop(0))

        conveyorBelt.append(currVal)
        orderedConveyorBelt.add(currVal)

    return [conveyorBelt, len(conveyorBelt)]
