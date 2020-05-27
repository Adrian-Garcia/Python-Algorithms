def solucion1():
  
  for i in range(100):
  
    num = i+1

    if (num % 5 == 0 and num % 3 == 0):
      print("hola adios")

    elif (num % 5 == 0):
      print("adios")

    elif (num % 3 == 0):
      print("hola")

    else:
      print(num)

def solucion2(frase):

	res = ''
	aux = ''

	i=0

	if (frase[len(frase)-1] != ' '):
		frase += ' '

	while (i < len(frase)):

		if (frase[i] != ' '):
			aux += frase[i]

		else:

			j = len(aux)-1

			while (j >= 0):
				res += aux[j]
				j-=1

			res += ' '
			aux = ''
			
		i+=1

	return res


def solucion3(palabra):

	a = [0] * 256

	bigNum = 0
	bigLet = ''

	for i in palabra:

		a[ord(i)] += 1

		if bigNum < a[ord(i)]:
			bigNum = a[ord(i)]
			bigLet = i

	return bigLet

def quitarEspaciosYHacerMinuscula(frase):

	newFrase = ''

	for i in frase:
		if i != ' ':
			newFrase += i

	return newFrase.lower()

def solucion4(frase):

	newFrase = quitarEspaciosYHacerMinuscula(frase)
	a = 0 if (len(newFrase) % 2 == 0) else 1

	sub1 = newFrase[0:int(len(newFrase)/2)]
	sub2 = newFrase[int(len(newFrase)/2 + a) : int(len(newFrase))]

	if (sub1 == sub2[::-1]):
		return True

	return False

# solucion1()
# print(solucion2('hola adios'))
# print (solucion3('bbaa'))
# print(solucion4('Anita Lava La tina'))