def readListAdj(listAdj, e):

	print("Insert Graph Edge and arch")

	for i in range(e):

		a = int(input())
		b = int(input())

		listAdj[a-1].append(b-1)
		listAdj[b-1].append(a-1)

def printListAdj(listAdj):

	for i in range(len(listAdj)):
		print("{} -> ".format(i+1), end='')

		for j in range(len(listAdj[i])):

			if j != 0:
				print(" - ", end='')

			print(listAdj[i][j]+1, end='')

		print()

print("Insert Edges and Arches")
v = int(input())
e = int(input())

listAdj = [[]] * v

readListAdj(listAdj, e)
printListAdj(listAdj)