import heapq

def calculate_distances(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priorityQueue = [(0, start)]
    while len(priorityQueue):
        currDist, currVertex = heapq.heappop(priorityQueue)

        if currDist > distances[currVertex]:
            continue

        for neighbor, weight in graph[currVertex].items():
            distance = currDist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priorityQueue, (distance, neighbor))

    return distances

graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print(calculate_distances(graph, 'X'))      # X => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
