# Programación orientada a objetos

# Definicion de una clase
class Persona:

	def __init__(self, nombre, apellido, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def presentacion(self):
		print("Mi nombre es {} {} tengo {} años".format(self.nombre, self.apellido, self.edad));

# Herencia
class Estudiante(Persona):

	def __init__(self, nombre, apellido, edad, carrera):
		super().__init__(nombre, apellido, edad)
		self.carrera = carrera

	def presentacion(self):
		print("Mi nombre es {} {} tengo {} anios y estudio {}".format(self.nombre, self.apellido, self.edad, self.carrera));

# Encapsulamiento
class Escuela():

	def __init__(self, nombre, estado, ranking, estudiantes):
		self.nombre = nombre
		self.estado = estado
		self.ranking = ranking
		self.estudiantes = estudiantes

	def descripcion(self):

		print("El {} se encuentra en {}. Ocupa el lugar {} nacional".format(self.nombre, self.estado, self.ranking))
		print("Sus estudiantes son: ", end ='')

		for i in self.estudiantes:
			print ("{} ".format(i.nombre), end='')

# Polimorfismo
class EscuelaIngenieria(Estudiante):

	def __init__(self, nombre, apellido, edad, carrera, materias):
		super().__init__(nombre, apellido, edad, carrera)
		self.materias = materias

	def presentacion(self):

		print("Soy {} y estoy en escuela de ingenieria".format(self.nombre))

		print("Mis materias son: ", end='')
		for i in self.materias:
			print("{} ".format(i), end="")

		print("\n")

# Polimorfismo
class EscuelaSalud(Estudiante):

	def __init__(self, nombre, apellido, edad, carrera, materias):
		super().__init__(nombre, apellido, edad, carrera)
		self.materias = materias

	def presentacion(self):

		print("Soy {} y estoy en escuela de salud".format(self.nombre))

		print("Mis materias son: ", end='')
		for i in self.materias:
			print("{} ".format(i), end="")

		print("\n")

# Sobrecarga de operadores
class Fraccion():

	def __init__(self, numerador, denominador):
		self.numerador = numerador
		self.denominador = denominador

	def __mul__(self, fracc):
		return Fraccion(self.numerador * fracc.numerador, self.denominador * fracc.denominador)

	def printFraccion(self):
		print ("{}/{}".format(self.numerador, self.denominador))

# Abstraccion
Fer = Persona("Fer", "Manzanita", 15)

# Herencia
Adrian = Estudiante("Adrian", "Garcia", 20, "ITC")

# Encapsulacion
Fernanda = Estudiante("Fer", "Manzanita", 20, "LPC")
Estudiantes = [Adrian, Fernanda]
ITESM = Escuela("ITESM", "MTY", 1, Estudiantes)

# Polimorfismo
TecIngenieria = EscuelaIngenieria("Adrian", "Garcia", 20, "ITC", ["Intro", 
"Mate"])
TecSalud = EscuelaSalud("Fer", "Manzanita", 20, "LPC", ["Intro", "EVAP"])

# Sobre carga de operadores
Fracc1 = Fraccion(1,2)
Fracc2 = Fraccion(2,3)
Fracc3 = Fracc1 * Fracc2

#Fer.presentacion()
#Adrian.presentacion()
#ITESM.descripcion()
#TecIngenieria.presentacion()
#TecSalud.presentacion()
#Fracc3.printFraccion()
