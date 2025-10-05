#This program is written to demonstrate the basics of numpy library in python
import numpy as np

#Creating a numpy array
arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)

#Operations on numpy array
arr2 = arr * arr
print("Element-wise Multiplication:", arr2)

#Calculating mean
mean_value = np.mean(arr2)
print("Mean of the array:", mean_value)

#Calculating standard deviation
std_dev = np.std(arr2)
print("Standard Deviation of the array:", std_dev)