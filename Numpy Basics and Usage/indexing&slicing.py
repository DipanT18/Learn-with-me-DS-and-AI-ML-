#This program is written to demonstrate the indexing and slicing of numpy arrays

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original Array:", arr)

#Indexing
print("Element at index 0 : ", arr[0])  #First element
print("Element at index 3 : ", arr[3])  #Fourth element
print("Element at index -1 : ", arr[-1]) #Last element
print("Element at index -3 : ", arr[-3]) #Third last element

#Slicing
print("Elements from index 2 to 5 : :", arr[2:6])  #Elements from index 2 to 5
print("Elements from start to index 4 : ", arr[:5]) #Elements from start to index 4
print("Elements from index 5 to end : ", arr[5:])  #Elements    from index 5 to end
print("Elements from start to end with step 2 : ", arr[::2]) #Elements from start to end with step 2
print("Elements from index 1 to 8 with step 3 : ", arr[1:9:3]) #Elements from index 1 to 8 with step 3

#Reversing the array
print("Reversed Array : ", arr[::-1]) #Reversed array

#Boolean Indexing
print(f"Elements greater than 50 : ", arr[arr > 50]) #Elements greater than 50
print(f"Elements less than or equal to 50 : ", arr[arr <= 50]) #Elements less than or equal to 50
print(f"Even Elements : ", arr[arr % 2 == 0]) #Even elements
print(f"Odd Elements : ", arr[arr % 2 != 0]) #Odd elements


#Modifying elements using indexing and slicing
arr[0] = 15 #Modifying first element
print("Array after modifying first element: ", arr)

arr[2:5] = [35, 45, 55] #Modifying elements from index 2 to 4
print("Array after modifying elements from index 2 to 4: ", arr)

arr[arr > 50] = 0 #Setting all elements greater than 50 to 0
print("Array after setting elements greater than 50 to 0: ", arr)