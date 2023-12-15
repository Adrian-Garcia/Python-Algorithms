"""
Implement dijstra using the follwing class definition:
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""
import heapq


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else {}

    def dijkstra(self, goal):
        pass


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n0.neighbors = {n1: 2, n2: 3, n4: 3}
n1.neighbors = {n0: 2, n5: 1}
n2.neighbors = {n0: 3, n3: 3, n6: 5}
n3.neighbors = {n2: 3, n4: 2, n7: 9}
n4.neighbors = {n3: 2, n0: 3}
n5.neighbors = {n1: 1}
n6.neighbors = {n2: 5}
n7.neighbors = {n3: 9}
