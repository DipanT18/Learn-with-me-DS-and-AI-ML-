#This program is written to demonstrate the way/method or syntax of creating arrays pf different types in python
#Array is defined as a collection of items stored at contiguous memory locations.
import numpy as np

#From a list
arr1 = np.array([1,2,3,4,5])
print("Array from a list: ", arr1)

#From a tuple
arr2 = np.array((1,2,3,4,5))
print("Array from a tuple: ", arr2)

#Array of zeros
arr3 = np.zeros((3, 4)) #3 rows and 4 columns
print("Array of zeros: \n", arr3)

#Array of ones
arr4 = np.ones((2, 5)) #2 rows and 5 columns
print("Array of ones: \n", arr4)

#Array with a specific value
arr5 = np.full((3, 3), (7, 4, 5)) #3x3 array
print("Array with a specific value: \n", arr5)

#Array with random values
arr6 = np.random.rand(3, 2) #3 rows and 2 columns
print("Array with random values: \n", arr6)

#Array with a range of values
arr7 = np.arange(0, 10, 2) #From 0 to 10 with a step of 2
print("Array with a range of values: ", arr7)

#Array with evenly spaced values
arr8 = np.linspace(0, 1, 5) #5 values from 0 to 1
print("Array with evenly spaced values: ", arr8)

#Identity matrix
arr9 = np.eye(3) #3x3 identity matrix
print("Identity matrix: \n", arr9)

#Empty array (uninitialized values)
arr10 = np.empty((2, 3)) #2 rows and 3 columns
print("Empty array (uninitialized values): \n", arr10)

#Array from existing data (copy)
data = [1, 0, 8, 5, 3]
arr11 = np.array(data)
print("Array from existing data (copy): ", arr11)

#Array from existing data (view)
arr12 = np.asarray(data)
print("Array from existing data (view): ", arr12)

#Array with a specific data type
arr13 = np.array([1, 2, 3.7], dtype=np.float64)   
print("Array with a specific data type: ", arr13)

#Scalar array
arr14 = np.array(42) #Single value array
print("Scalar array: ", arr14)

#Structured array
dtype = [('name', 'S10'), ('age', 'i4'), ('height', 'f4')]
values = [('Alice', 25, 5.5), ('Bob', 30, 6.0)]
arr15 = np.array(values, dtype=dtype)
print("Structured array: \n", arr15)

#Matrix of different elements
arr16 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix of different elements: \n", arr16)

#3D array
arr17 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D array: \n", arr17)    

#Array from a generator
arr18 = np.fromiter(range(5), dtype=int)
print("Array from a generator: ", arr18)