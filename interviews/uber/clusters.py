# Given an adjacency matrix for an undirected finite graph, find the distinct clusters formed by the nodes in the graph.
# Example 1:
#   A B C D E
# A [0 1 0 0 0]
# B [1 0 1 0 0]
# C [0 1 0 0 0]
# D [0 0 0 0 1]
# E [0 0 0 1 0]
# Edge: A - B, B - C, D - E
# Output: [(A, B, C), (D, E)]

# Output: [(A,B), (C)]

# nodeNames = [A,B,C]
# nodeVisited = [1,1,0]

# clusters = [[A, B], [C]]
# queue = []

# import requests
# import mysql.connector
# import pandas as pd


def getClusterByDFS(queue, clusters, graph, nodeNames, nodeVisited):

    while len(queue) != 0:
        current = queue[0]  # C
        position = nodeNames.index(current)  # 2
        nodeVisited[position] = True

        for i in range(len(graph[position])):
            if graph[position][i] and not nodeVisited[i]:
                queue.append(nodeNames[i])

        clusters[len(clusters) - 1].append(current)
        queue.pop(0)


def clusters(graph):

    # Change implementarion for this nodeNames. They should not be hardcoded
    nodeNames = ["A", "B", "C", "D", "E"]  # [A, B, C]
    nodeVisited = [False] * len(graph)  # [1, 1, 1]
    clusters = []  # [[A, B], [C]]
    queue = []  # []

    for i in range(len(graph)):
        current = nodeNames[i]  # A

        if not nodeVisited[i]:
            nodeVisited[i] = True
            queue.append(current)
            clusters.append([])
            getClusterByDFS(queue, clusters, graph, nodeNames, nodeVisited)

    return clusters


#   A B C
# A 0 1 0
# B 1 0 0
# C 0 0 0

# firstInput = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]

#   A B C D E
# A [0 1 0 0 0]
# B [1 0 1 0 0]
# C [0 1 0 0 0]
# D [0 0 0 0 1]
# E [0 0 0 1 0]

secondInput = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
]

print(clusters(secondInput))
