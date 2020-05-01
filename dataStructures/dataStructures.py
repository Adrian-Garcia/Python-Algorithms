# Estructuras de datos
import queue

# Vector
def vector():

	myVector = []

	myVector.append(1)
	myVector.append(2)
	myVector.append(3)
	myVector.append(4)

	for i in myVector:
		print (i, end = ' ')
	print()

	myVector.remove(myVector[0])
	for i in myVector:
		print (i, end = ' ')
	print()

# Queue
def	queueFunction():

	q = queue.Queue(10)

	q.put(1)
	q.put(2)
	q.put(3)
	q.put(4)
	q.put(5)
	q.put(6)

	while (not q.empty()):
		print(q.get())
	print()

# Stack
def stackFunction():

	q = queue.LifoQueue(10)

	q.put(1)
	q.put(2)
	q.put(3)
	q.put(4)
	q.put(5)
	q.put(6)

	while (not q.empty()):
		print(q.get())
	print()

# PriorityQueue
def priorityQueue():

	q = queue.PriorityQueue(10)

	q.put(2)
	q.put(6)
	q.put(1)
	q.put(4)
	q.put(3)
	q.put(5)

	while (not q.empty()):
		print(q.get())
	print()

def set():

	mySet = {"Delete"}

	mySet.add("Fer")
	mySet.add("Adrian")
	mySet.add("Lucero")
	mySet.remove("Delete")

	for i in mySet:
		print(i, end = ' ')
	print()

	print("\nBuscando a Marrana...")
	if ("Marrana" in mySet):
		print ("Marrana fue encontrada")

	else:
		print("Marrana no fue encontrada")

# Dictionary (hash map)
def dictionary():

	myDictionary = {}

	myDictionary["a"] = 1
	myDictionary["b"] = 2
	myDictionary["c"] = 3
	myDictionary["d"] = 4
	myDictionary["f"] = 6
	myDictionary["e"] = 5
	myDictionary.pop("f")

	for i in myDictionary:
		print ("{} {}".format(i, myDictionary[i]))
	print()

	print("Buscando f...")
	if ("f" in myDictionary):
		print ("f fue encontrada")

	else:
		print ("f no fue encontrada")
