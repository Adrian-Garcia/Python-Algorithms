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

	def arraySlicing():
		pass

program = numpyTest()
program.arraySlicing()