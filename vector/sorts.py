def descendantSort():

	Personas = ["Adrian", "Fer", "Atenea", "Zeus"]

	print("Personas: ", end='')
	print(Personas)

	Personas.sort()
	print("Personas.sort(): ", end='')
	print(Personas)

def descendantSort():

	Numeros = [1,2,3,4,5]

	print("Numeros: ", end='')
	print(Numeros)

	Numeros.sort(reverse=True)
	print("Numeros.sort(reverse=True): ", end='')
	print(Numeros)

def customSort():
	
	def myFunc(e):
		return len(e)

	cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
	
	print("Cars: ", end='')
	print(cars)
	
	cars.sort(reverse=True, key=myFunc)
	print("Cars.sort(reverse=True, key=myFunc): ", end='')
	print(cars)


def mergeSort(arr): 

	if len(arr) >1: 

		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R): 

			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1

			else: 
				arr[k] = R[j] 
				j+= 1

			k+= 1

		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7] 
	print ("Given array is", end ="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end ="\n") 
	printList(arr) 

# This code is contributed by Mayank Khanna 
