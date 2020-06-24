''' 
NumPy
	Python library sed for working with arays
	Widely used in linear algebra, fourier transform and matrices
'''
import numpy as np

class numpyTest(object):
	
	def npArray(self):
		
		# base list
		arr = [1,2,3,4,5]

		# numpy array
		npArr = np.array(arr)
		print("Type Array: {}".format(type(npArr)))
		print("Array: {}\n". format(npArr))

		# regular array
		print("Type Array: {}".format(type(arr)))
		print("Array: {}". format(arr))
 
	def dimensions(self):

		# 0-D array
		arr0 = np.array(42)

		# 1-D array
		arr1 = np.array([1, 2, 3, 4, 5])

		# 2-D array		
		arr2 = np.array([[1, 2, 3], [4, 5, 6]])

		# 3-D aray
		arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

		# Display array sizes
		print("Array of {} dimensions. \nArray: ".format(arr0.ndim))
		print(arr0)

		print("\nArray of {} dimensions. \nArray: ".format(arr1.ndim))
		print(arr1)

		print("\nArray of {} dimensions. \nArray: ".format(arr2.ndim))
		print(arr2)

		print("\nArray of {} dimensions. \nArray: ".format(arr3.ndim))
		print(arr3)

		# Create an array with specific dimensions
		arr5 = np.array([1,2,3,4], ndmin=5)
		print("\nArray of {} dimensions. \nArray: ".format(arr5.ndim))
		print(arr5)

	def arrayIndexing(self):

		arr1 = np.array([1,2,3,4])
		print("arr1 = {}".format(arr1))
		print("arr1[0] = {}\n".format(arr1[0]))

		arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
		print("arr2 = {}".format(arr2))
		print("arr2[0,1] = {}".format(arr2[0,1]))

		arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
		print("arr3 = {}".format(arr3))
		print("arr3[0,1,2] = {}".format(arr3[0,1,2]))

	def arraySlicing(self):
	
		# 1-D Array
		arr = np.array([1, 2, 3, 4, 5, 6, 7])
		print("Array = {}".format(arr))
		print("Values of arr from index 1 to 5 = {}".format(arr[1:5]))
		print("Values of arr from index 4 (included 4)to end = {}".format(arr[4:]))
		print("Values of arr from start of indec to 4 (not included 4) = {}".format(arr[:4]))
		print("Values of arr from the end to index 1 from the end = {}".format(arr[-3:-1]))
		print("Values of arr from index 1 to index 5 (2 by 2) = {}".format(arr[1:5:2]))
		print("Values of arr from idnex 0 to 1 (2 by 2) = {}".format(arr[::2]))

		#2-D Array
		arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
		print("\nArray = {}".format(arr2))
		print("Values of arr2, second row from index 1 to 4  = {}".format(arr2[1,1:4]))
		print("Values of arr2, first and second row, index 2  = {}".format(arr2[0:2,2]))
		print("Values of arr2, first and second row, index 1 to 4  = {}".format(arr2[0:2, 1:4]))

	def copyVsView(self):

		arr = np.array([1, 2, 3, 4, 5])
		x = arr.copy()
		y = arr.view()

		print("arr = [1, 2, 3, 4, 5]")
		print("x = arr.copy() = {}".format(x))
		print("y = arr.view() = {}".format(y))
		print()

		x[0] = 0

		print("x[0] = 0")
		print("arr = {}".format(arr))
		print("x = {}".format(x))
		print("y = {}".format(y))
		print()

		y[0] = 0

		print("y[0] = 0")
		print("arr = {}".format(arr))
		print("x = {}".format(x))
		print("y = {}".format(y))

	def iterating(self):
		
		arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

		for x in arr:
			for y in x:
				for z in y:
					print(z, end='\t')
				print()

program = numpyTest()
program.iterating()