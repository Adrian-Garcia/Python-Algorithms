arr1 = [1,2,3,4]
arr2 = arr1
arr3 = arr1[:]
arr4 = arr3[::-1]

print("Arr1 = [1,2,3,4] = {}".format(arr1))
print("Arr2 = Arr1 = {}".format(arr2))
print("Arr3 = Arr1[:] = {}".format(arr3))

arr1.remove(4)

print("\nArr1.remove(4)\n")
print("Arr1 = {}".format(arr1))
print("Arr2 = {}".format(arr2))
print("Arr3 = {}".format(arr3))

print("\nArr4 = Arr3[::-1] = {}".format(arr4))