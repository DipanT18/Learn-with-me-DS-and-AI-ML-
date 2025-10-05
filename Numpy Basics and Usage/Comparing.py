#This code is written to demonstrate the comparison of numpy arrays with python lists
#Comparison means checking the equality or inequality of two arrays or lists
import numpy as np
import time

#Creating two numpy arrays
arr = np.array([1, 2, 3, 4, 5])
start_time = time.time()
Squared_arr = arr ** 2
print("Squared Numpy Array:", Squared_arr)
time1 = time.time() - start_time
print("Time taken for numpy array operation: %s seconds" % time1)

#Creating two python lists
list1 = [1, 2, 3, 4, 5]
start_time = time.time()
Squared_list = [x ** 2 for x in list1]
print("Squared Python List:", Squared_list)
time2 = time.time() - start_time
print("Time taken for python list operation: %s seconds" % time2)


