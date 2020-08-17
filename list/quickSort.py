def partition(arr, low, top):

	i = (low - 1)
	pivot = arr[top]

	for j in range(low, top):

		if arr[j] < pivot:

			i += 1 
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[top] = arr[top], arr[i+1]
	return (i+1)

def quickSort(arr, low, top):

	if low < top:

		partitionIndex = partition(arr, low, top)

		quickSort(arr, low, partitionIndex-1)
		quickSort(arr, partitionIndex+1, top)


myArray = [2,3,1]
print("myArray = {}".format(myArray))
quickSort(myArray, 0, len(myArray)-1)
print("myArray.sort() = {}".format(myArray))