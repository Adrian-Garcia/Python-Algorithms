lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listaConDuplicados = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
positionOfDuplicates = [i for i, x in enumerate(listaConDuplicados) if x == 2]

if 0 in lista:
    print("El 0 esta en la lista")

print("El 9 esta en la posicion {}".format(lista.index(9)))
print("Lista con duplicados = {}".format(listaConDuplicados))

print("Posicion de los 2s: {}".format(positionOfDuplicates))
