class GraphNode(object):

	def __init__ (self, val):
		self.val = val
		self.adjacent = {}

class Graph():

	def __init__ (self, start):
		self.start = start

	def breadthFirst(self):

		