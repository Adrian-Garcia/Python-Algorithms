import queue

class GraphNode(object):

	def __init__ (self, val):
		self.val = val
		self.adjacent = {}
		self.visited = False

	def printNode(self):
		print(self.val)

class Graph():

	def __init__ (self, start, nodeList):
		self.start = start	# Node in wich the graph beggins
		self.nodeList = nodeList

	def breadthFirst(self):
		
		nodes = queue.LifoQueue(len(self.nodeList))

		nodes.put(self.start)

		while (not nodes.empty()):

			curr = nodes.get()
			curr.visited = True
			print(curr.val)

			for i in curr.adjacent:
				if not curr.adjacent[i].visited:
					nodes.put(curr.adjacent[i])

node1 = GraphNode("Nuevo Leon")
node2 = GraphNode("San Luis")
node3 = GraphNode("Guanajuato")
node4 = GraphNode("Durango")
node5 = GraphNode("Zacatecas")

node1.adjacent["San Luis"] = node2
node1.adjacent["Zacatecas"] = node5
node2.adjacent["Nuevo Leon"] = node1
node2.adjacent["Zacatecas"] = node5
node2.adjacent["Guanajuato"] = node3 
node3.adjacent["San Luis"] = node2
node3.adjacent["Zacatecas"] = node5
node4.adjacent["Zacatecas"] = node5
node5.adjacent["Nuevo Luis"] = node1
node5.adjacent["San Luis"] = node2
node5.adjacent["Guanajuato"] = node3
node5.adjacent["Durango"] = node5

nodeList = ["Nuevo Leon", "San Luis", "Guanajuato", "Durango", "Zacatecas"]

myGraph = Graph(node1, nodeList)
myGraph.breadthFirst()