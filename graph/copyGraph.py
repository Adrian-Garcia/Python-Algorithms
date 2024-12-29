""" 133. Clone Graph
Medium
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
    For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1,
    the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors
of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the
cloned graph.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.

Constraints:
    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be originalVisited starting from the given node.
"""

from typing import Optional


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        response = f"{self.val} -> ["

        for i in range(len(self.neighbors)):
            neighbor = self.neighbors[i]
            response += f"{neighbor.val}"
            if i < len(self.neighbors) - 1:
                response += " "

        return response + "]"


class Solution(object):
    def cloneGraph(self, node: Optional[Node]) -> Node:
        if not node:
            return

        newStartNode = Node(node.val)
        originalVisited = set()
        newVisited = dict()

        originalQueue = [node]
        newQueue = [newStartNode]

        while len(originalQueue):
            originalNode = originalQueue.pop(0)
            newNode = newQueue.pop(0)

            if originalNode in originalVisited:
                continue

            originalVisited.add(originalNode)
            newVisited[newNode.val] = newNode

            for neighbor in originalNode.neighbors:
                if neighbor.val in newVisited:
                    newNeighbor = newVisited[neighbor.val]
                else:
                    newNeighbor = Node(neighbor.val)
                    newVisited[newNeighbor.val] = newNeighbor

                newNode.neighbors.append(newNeighbor)
                newQueue.append(newNeighbor)
                originalQueue.append(neighbor)

        return newStartNode


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

newNode1 = Solution().cloneGraph(node1)
newNode2 = newNode1.neighbors[0]
newNode4 = newNode1.neighbors[1]
newNode3 = newNode2.neighbors[1]

print("\n\n")
print("newNode1.val", newNode1.val, hex(id(newNode1)))
print("newNode2.val", newNode2.val, hex(id(newNode2)))
print("newNode3.val", newNode3.val, hex(id(newNode3)))
print("newNode4.val", newNode4.val, hex(id(newNode4)))

print("\nnewNode1", newNode1)
print("newNode2", newNode2)
print("newNode3", newNode3)
print("newNode4", newNode4)

print("\nnewNode1.neighbors", newNode1.neighbors)
print("newNode2.neighbors", newNode2.neighbors)
print("newNode3.neighbors", newNode3.neighbors)
print("newNode4.neighbors", newNode4.neighbors)
