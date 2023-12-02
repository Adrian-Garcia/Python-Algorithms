"""
Data Structure for graphs. 
  - DFS 
  - BFS 
"""


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def breadthFirstSearch(self):
        queue = [self]
        visited = {self.val}

        return_nodes = list()
        return_values = list()

        while queue:
            curr_node = queue.pop(0)

            return_nodes.append(curr_node)
            return_values.append(curr_node.val)

            for neighbor in curr_node.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor.val)

        return return_nodes, return_values

    def deepFirstSearch(self):
        stack = [self]
        visited = {self.val}

        return_nodes = list()
        return_values = list()

        while stack:
            curr_node = stack.pop()

            return_nodes.append(curr_node)
            return_values.append(curr_node.val)

            for neighbor in reversed(curr_node.neighbors):
                if neighbor.val not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor.val)

        return return_nodes, return_values


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# return_nodes_bfs, return_values_bfs = node1.breadthFirstSearch()
# print("return_values_bfs =", return_values_bfs)

# return_nodes_dfs, return_values_dfs = node1.deepFirstSearch()
# print("return_values_dfs =", return_values_dfs)

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n0.neighbors = [n3, n4]
n1.neighbors = [n2, n5, n6]
n2.neighbors = [n1, n5]
n3.neighbors = [n0, n5, n7]
n4.neighbors = [n0, n6]
n5.neighbors = [n1, n2, n3, n7]
n6.neighbors = [n1, n4, n7]
n7.neighbors = [n3, n5, n6]

return_nodes_bfs, return_values_bfs = n0.breadthFirstSearch()
print("return_values_bfs =", return_values_bfs)

return_nodes_dfs, return_values_dfs = n0.deepFirstSearch()
print("return_values_dfs =", return_values_dfs)
