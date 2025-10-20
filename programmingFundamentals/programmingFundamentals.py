# Fundamentos de programacion en python
import sys

# Declaracion de variables
def DeclaracionVariables():

    edad = 20
    nombre = "Fer"
    apellido = "Martinez"
    estatura = 1.55

    print(
        "La niña más bonita es {} {}. Tiene {} años y mide {}m".format(
            nombre, apellido, edad, estatura
        )
    )


# Condicionales
def Condicionales():

    niniaBonita = "Fer Manzanita"
    nombre = input("\nPara continuar, di quién es la niña más bonita: ")

    if nombre == niniaBonita:
        print("¡Correcto!")

    else:
        print("¡Incorrecto!")
        sys.exit()


# Operadores
def Operadores():

    edad = 20
    nombre = "Fer"
    apellido1 = "Manzanita"
    apellido2 = "Martinez"

    inEdad = int(input("Inserta una edad: "))
    inNombre = input("Inserta un nombre: ")
    inApellido = input("Inserta un apellido: ")

    if (
        inEdad == edad
        and inNombre == nombre
        and (inApellido == apellido1 or inApellido == apellido2)
    ):
        print("Esa es Fer Manzanita")

    else:
        print("Esa no es Fer Manzanita")


# Bit manipulation
def BitManipulation():

    # Convierte un numero de cierta base a entero
    print("Binary 1010   ->   {}".format(int("1010", 2)))
    print("Terciary 120  ->   {}\n".format(int("120", 3)))

    # Otras compuertas lógicas
    print("1 XOR 0  ->  {}".format(1 ^ 0))
    print("1 AND 0  ->  {}".format(1 and 0))
    print("1 OR 0   ->  {}".format(1 or 0))
    print("1 NOT    ->  {}".format(not 1))


# Operaciones
def Operaciones():

    print("2+5  = {}".format(2 + 5))
    print("2-5  = {}".format(2 - 5))
    print("2*5  = {}".format(2 * 5))
    print("2/5  = {}".format(2 / 5))
    print("2%5  = {}".format(2 % 5))
    print("2**5 = {}".format(2**5))
    print("2//5 = {}".format(2 // 5))


# Loops
def Loops():

    print("\nCuenta del 0 al 10: ", end="")

    for i in range(11):
        print("{} ".format(i), end="")

    print("\nCuenta del 10 al 100 en decenas: ", end="")

    for i in range(10, 110, 10):
        print("{} ".format(i), end="")

    name = "Not Fer"
    print("\n")

    while name != "Fer":
        name = input("Para salir debes escribir Fer: ")


# Arreglos
def Arreglos():

    cosasLindasDeFer = ["Carita", "Ojos", "Boca", "Cabello"]

    print("\nCosas bonitas de Fer: ", end="")
    for i in cosasLindasDeFer:
        print("{} ".format(i), end="")

    # regresar un objeto o valor
    return cosasLindasDeFer


# Arreglos que utilizam memoria de forma dinamica
def Vectores():

    array = Arreglos()
    objeto = input("\n\nAgrega una nueva: ")
    array.append(objeto)

    print("\nCosas bonitas de Fer: ", end="")
    for i in array:
        print("{} ".format(i), end="")


# Matrices
def Matrices():

    # Declarar matrices forma 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Declarar matrices forma 2
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Recorrer matriz
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            print("{} ".format(matrix1[i][j]), end="")
        print()
    print()

    # Añadir un valor a un renglón de la matriz
    matrix2[1].append(6)
    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            print("{} ".format(matrix2[i][j]), end="")
        print()
    print()

    # Crear una matrix de dimenciones establecidas
    print("¡Vamos a crear una matriz!")
    filas = int(input("Inserta el tamaño de filas: "))
    columnas = int(input("Inserta el tamaño de columnas: "))

    matrix = [[0 for x in range(columnas)] for i in range(filas)]
    print("Matriz[{}][{}]\n".format(len(matrix), len(matrix[0])))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = input()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], " ", end="")
        print()
    print()


# DeclaracionVariables()
# Condicionales()
# Operadores()
# BitManipulation()
# Operaciones()
# Loops()
# Arreglos()
# Vectores()
# Matrices()
