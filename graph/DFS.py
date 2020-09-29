from collections import defaultdict 

class Graph:

	def __init__(self):
		self.graph = {} 

	def addEdge(self, u, v):
		
		if u in self.graph:
			self.graph[u].append(v)

		else:
			self.graph[u] = [v]

	def DFS(self, s):

		visited = [False] * (len(self.graph))
		queue = []

		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop()
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print ("DFS: ", end='')
g.DFS(2)
print()

# This code is contributed by Neelam Yadav 
