#This program is written to demonstrate the reshaping and combining of numpy arrays
#Reshaping means changing the shape of an array without changing its data
#Combining means joining two or more arrays into a single array

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Original Array:\n", arr)

#Reshaping the array to 4x2
reshaped_arr = arr.reshape(4, 2)
print("Reshaped Array (4x2):\n", reshaped_arr)

#Combining the original and reshaped arrays
try:
    combined_arr = np.concatenate((arr, reshaped_arr), axis=1)  # This will raise an error
    print("Combined Array:\n", combined_arr)
except ValueError as e:
    print("Error occurred while combining arrays:", e)

#Flattening the original array
flattened_arr = arr.flatten() # ----> Flattening means converting a multi-dimensional array into a one-dimensional array
print("Flattened Array:\n", flattened_arr)

#Stacking arrays vertically
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
stacked_arr = np.vstack((arr1, arr2)) # ----> Stacking means joining arrays along a new axis
print("Stacked Array (Vertical):\n", stacked_arr)


#Stacking arrays horizontally
stacked_arr_h = np.hstack((arr1, arr2)) # ----> Stacking means joining arrays along a new axis
print("Stacked Array (Horizontal):\n", stacked_arr_h)

#Splitting the stacked array into two arrays
split_arr = np.vsplit(stacked_arr, 2) # ----> Splitting means dividing an array into multiple sub-arrays
print("Split Arrays (Vertical):\n", split_arr)
#Splitting the stacked array horizontally into two arrays
split_arr_h = np.hsplit(stacked_arr_h, 2) # ----> Splitting means dividing an array into multiple sub-arrays
print("Split Arrays (Horizontal):\n", split_arr_h)
