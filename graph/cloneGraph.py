"""
Correct solution in copyGraph.py

133. Clone Graph
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
    The Graph is connected and all nodes can be visited starting from the given node.
"""
from typing import Optional

class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def getNodeNeighbors(self):
        neighbor_names = list()
        for neighbor in self.neighbors:
            neighbor_names.append(neighbor.val)
        return neighbor_names


class Solution(object):
    def cloneGraph(self, node: Optional[Node]) -> Node:
        if not node:
            return

        newStartNode = Node(node.val)
        originalVisited = dict()
        newVisited = dict()

        originalQueue = [node]
        newQueue = [newStartNode]

        while len(originalQueue):
            originalNode = originalQueue.pop(0)
            newNode = newQueue.pop(0)

            if originalNode in originalVisited:
                continue

            originalVisited[originalNode] = newNode
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

    def __getNewNode(self, new_graph, curr_node):
        if curr_node.val in new_graph:
            return new_graph[curr_node.val]
        else:
            return Node(curr_node.val)

    def cloneGraphFails(self, node):
        if not node:
            return

        queue = [node]
        visited = set()
        start = None
        new_graph = dict()

        while queue:
            curr_node = queue.pop(0)

            if curr_node.val in visited:
                continue

            new_node = self.__getNewNode(new_graph, curr_node)

            visited.add(curr_node.val)

            if not start:
                start = new_node

            for neighbor in curr_node.neighbors:
                new_neighbor = None

                if neighbor.val in new_graph:
                    new_neighbor = new_graph[neighbor.val]

                else:
                    new_neighbor = Node(neighbor.val)
                    new_graph[new_neighbor.val] = new_neighbor

                if neighbor.val not in visited:
                    queue.append(neighbor)

                new_node.neighbors.append(new_neighbor)

        return start

    def cloneGraphDontWork(self, node):
        visited = set()
        queue = [node]
        start = None
        new_graph = dict()

        while queue:
            curr_node = queue.pop(0)
            new_node = Node(curr_node.val)
            curr_node_val = new_node.val

            if not start:
                start = new_node

            visited.add(curr_node_val)
            new_graph[curr_node.val] = curr_node

            for curr_neighbor in curr_node.neighbors:
                # print(neighbor)
                print(len(curr_node.neighbors))

                neighbor_val = curr_neighbor.val
                new_neighbor = None

                if curr_neighbor.val in new_graph:
                    new_neighbor = new_graph[curr_neighbor.val]

                else:
                    new_neighbor = Node(curr_neighbor.val)
                    new_graph[curr_neighbor.val] = new_neighbor

                new_neighbor.neighbors.append(new_neighbor)

                if curr_neighbor.val not in visited:
                    queue.append(new_neighbor)

        return start


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
new_node1 = solution.cloneGraph(node1)
new_node2 = new_node1.neighbors[0]
new_node3 = new_node2.neighbors[1]
new_node4 = new_node1.neighbors[1]

print("========== original ==========\n")

print("node1 ->", node1)
print("node2 ->", node2)
print("node3 ->", node3)
print("node4 ->", node4)

print("\nnode1 ->", node1.val)
print("node2 ->", node2.val)
print("node3 ->", node3.val)
print("node4 ->", node4.val)

print("\nnode1 neighbros ->", node1.getNodeNeighbors())
print("node2 neighbros ->", node2.getNodeNeighbors())
print("node3 neighbros ->", node3.getNodeNeighbors())
print("node4 neighbros ->", node4.getNodeNeighbors())

print("\n\n========== new ==========\n")

print("new_node1 ->", new_node1)
print("new_node2 ->", new_node2)
print("new_node3 ->", new_node3)
print("new_node4 ->", new_node4)


print("\nnew_node1 ->", new_node1.val)
print("new_node2 ->", new_node2.val)
print("new_node3 ->", new_node3.val)
print("new_node4 ->", new_node4.val)

print("\nnew_node1 neighbros ->", new_node1.getNodeNeighbors())
print("new_node2 neighbros ->", new_node2.getNodeNeighbors())
print("new_node3 neighbros ->", new_node3.getNodeNeighbors())
print("new_node4 neighbros ->", new_node4.getNodeNeighbors())
