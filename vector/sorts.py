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

customSort()