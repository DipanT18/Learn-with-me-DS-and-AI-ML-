#This program is written to demonstrate the basic operations that can be performed on numpy arrays

import numpy as np

#Creating two numpy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

#Element-wise addition
arr_sum = arr1 + arr2
print("Element-wise Addition:", arr_sum)

#Element-wise subtraction
arr_diff = arr2 - arr1
print("Element-wise Subtraction:", arr_diff)

#Element-wise multiplication
arr_prod = arr1 * arr2
print("Element-wise Multiplication:", arr_prod)

#Element-wise division
arr_div = arr2 / arr1
print("Element-wise Division:", arr_div)

#This was normal calculation but numpy provides many built-in functions to perform operations on arrays
#Now moving to vector and matrix calculations

#Creating two 2D numpy arrays (matrices)
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
added_matrix = mat1 + mat2
print("Matrix Addition:\n", added_matrix)

#Matrix multiplication
multiplied_matrix = np.dot(mat1, mat2)
print("Matrix Multiplication:\n", multiplied_matrix)

#Calculating the transpose of a matrix
transposed_matrix = np.transpose(mat1)
print("Matrix Transpose:\n", transposed_matrix)

#Calculating the determinant of a matrix
determinant1 = np.linalg.det(mat1)
print("Determinant of the matrix:", determinant1)
determinant2 = np.linalg.det(mat2)
print("Determinant of the matrix:", determinant2)

#Calculating the inverse of a matrix
inverse_matrix = np.linalg.inv(mat1)
print("Matrix Inverse:\n", inverse_matrix)
#Verifying the inverse by multiplying with the original matrix
identity_matrix = np.dot(mat1, inverse_matrix)
print("Identity Matrix:\n", identity_matrix)

#Calculating eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(mat1)
print("Eigenvalues of the matrix:", eigenvalues)
print("Eigenvectors of the matrix:\n", eigenvectors)
#Verifying the eigenvalue equation
for i in range(len(eigenvalues)):
    left_side = np.dot(mat1, eigenvectors[:, i])
    right_side = eigenvalues[i] * eigenvectors[:, i]
    print(f"Verification for eigenvalue {eigenvalues[i]}: Left Side = {left_side}, Right Side = {right_side}")

#Calculating the rank of a matrix
rank = np.linalg.matrix_rank(mat1)
print("Rank of the matrix:", rank)