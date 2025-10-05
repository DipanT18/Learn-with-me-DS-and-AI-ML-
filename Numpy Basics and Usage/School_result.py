#This is the real world example of numpy library

import numpy as np
#Creating a numpy array to store the marks of students in different subjects
names_of_students = ['Robin', 'Boob', 'Chipley', 'Daka', 'Nasha']
maths_marks = np.array([85, 78, 90, 66, 59])
science_marks = np.array([92, 88, 95, 70, 60])

#Calculating the average marks
average_Maths_marks = np.mean(maths_marks)
print("Average Maths Marks:", average_Maths_marks)

average_Science_marks = np.mean(science_marks)
print("Average Science Marks:", average_Science_marks)

average_total_marks = np.mean(maths_marks + science_marks)
print("Average Total Marks:", average_total_marks)

#Calculating the highest marks
highest_Maths_marks = np.max(maths_marks)
print("Highest Maths Marks:", highest_Maths_marks)

highest_Science_marks = np.max(science_marks)
print("Highest Science Marks:", highest_Science_marks)

highest_among_both = np.max(np.concatenate((maths_marks, science_marks)))
print("Highest Marks among both subjects:", highest_among_both)

#Calculating the lowest marks
lowest_Maths_marks = np.min(maths_marks)
print("Lowest Maths Marks:", lowest_Maths_marks)

lowest_Science_marks = np.min(science_marks)
print("Lowest Science Marks:", lowest_Science_marks)

lowest_among_both = np.min(np.concatenate((maths_marks, science_marks)))
print("Lowest Marks among both subjects:", lowest_among_both)

#Finding the top student based on total marks
total_marks = maths_marks + science_marks
top_student_index = np.argmax(total_marks)
print("Top Student:", names_of_students[top_student_index])
