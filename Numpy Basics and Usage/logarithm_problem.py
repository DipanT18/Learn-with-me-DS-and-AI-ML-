#This program demonstrate the use of logarithm in python (numpy) to solve the problem.

import numpy as np
Initial_Bacteria_count = 500
Final_Bacteria_count = 2000
time = 5 

Growth_Rate = (np.log(Final_Bacteria_count/Initial_Bacteria_count)) / time

print(f"The Growth Rate of Bacteria is : {Growth_Rate}")
