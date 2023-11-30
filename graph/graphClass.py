class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def breadthFirstSearch(self):
        queue = [self]
        visited = set()

        return_nodes = list()
        return_values = list()

        while queue:
            curr_node = queue.pop(0)

            return_nodes.append(curr_node)
            return_values.append(curr_node.val)
            visited.add(curr_node.val)

            for neighbor in curr_node.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor.val)

        return return_nodes, return_values

    def deepFirstSearch(self):
        stack = [self]
        visited = set()

        return_nodes = list()
        return_values = list()

        while stack:
            curr_node = stack.pop()

            return_nodes.append(curr_node)
            return_values.append(curr_node.val)
            visited.add(curr_node.val)

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

return_nodes_bfs, return_values_bfs = node1.breadthFirstSearch()
print("return_values_bfs =", return_values_bfs)

return_nodes_dfs, return_values_dfs = node1.deepFirstSearch()
print("return_values_dfs =", return_values_dfs)
