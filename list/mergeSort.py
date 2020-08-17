def mergeSort(arr):

	if len(arr) > 1:

		mid = len(arr) // 2

		arrLeft = arr[:mid]
		arrRight = arr[mid:]

		mergeSort(arrLeft)
		mergeSort(arrRight)

		i = 0
		j = 0
		k = 0

		while i < len(arrLeft) and j < len(arrRight):

			if arrLeft[i] < arrRight[j]:
				arr[k] = arrLeft[i]
				i += 1

			else:
				arr[k] = arrRight[j]
				j += 1

			k += 1

		while i < len(arrLeft):
			arr[k] = arrLeft[i]
			i += 1
			k += 1

		while j < len(arrRight):
			arr[k] = arrRight[j]
			j += 1
			k += 1

myArray = [2,3,1]
print("myArray = {}".format(myArray))
mergeSort(myArray)
print("myArray.sort() = {}".format(myArray))


