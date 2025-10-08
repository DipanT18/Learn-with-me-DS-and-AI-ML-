# This program is written to manage and analyze a student's result dataset using pandas library, numpy library and OOPs in Python.

import pandas as pd
import numpy as np

# A dictionary containing the student result data
dataframe = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Maths': [85, 92, 78, 90, 22, 76, 95, 69],
    'Science': [90, 85, 58, 92, 21, 80, 97, 73],
    'English': [78, 80, 55, 88, 38, 82, 94, 76],
    'History': [32, 75, 78, 85, 19, 82, 90, 67]
}

# The class to manage and analyze the student data
class Result:
    def __init__(self, dataframe):
        # Store a copy of the dataframe as an instance attribute
        self.df = dataframe.copy()

    # Method to calculate average marks of specified subjects
    # It only needs 'self' as it uses the instance's dataframe (self.df)
    def average_marks(self):
        # The .mean() function correctly computes the average of the specified columns
        return self.df[['Maths', 'Science', 'English', 'History']].mean()
    
    def maximum_marks(self):
        return self.df[['Maths', 'Science', 'English', 'History']].max()
    
    def miminum_marks(self):
        return self.df[['Maths', 'Science', 'English', 'History']].min()
    
#Now collecting result of each student:

class StudentReport:
    """A class to generate a detailed report for a single student."""

    def __init__(self, df, student_name):
        self.student_name = student_name
        self.student_data = df[df['Name'] == student_name]

        if self.student_data.empty:  # ✅ Fixed - no parentheses
            print(f"Error: Student named '{student_name}' not found in the DataFrame.")
        else:
            self.student_data = self.student_data.fillna(0)
            print(f"Student data for '{student_name}' has been loaded successfully.")

    def get_percentage(self):
        if self.student_data.empty:  # ✅ Fixed here too
            return "N/A"
    # ... rest of your code
    #Selects the score columns and convert them into numoy array
        numeric_scores = self.student_data.drop('Name', axis = 1, errors = 'ignore').values
        scores_array =numeric_scores.flatten()
        total_possible = 100 * len(scores_array) 
        total_obtained = np.sum(scores_array)
        percentage = (total_obtained/total_possible) * 100
        return percentage
    
    def get_grade(self):
        if self.student_data.empty:
            return "N/A"
    
    # Get the percentage by calling the method
        percentage = self.get_percentage()
    
    # Now check the grade based on percentage
        if percentage >= 90:
            return "A+"
        elif percentage >= 80 and percentage < 90:
            return "A"
        elif percentage >= 70 and percentage < 80:
            return "B+"
        elif percentage >= 60 and percentage < 70:
            return "B"
        elif percentage >= 50 and percentage < 60:
            return "C+"
        elif percentage >= 40 and percentage < 50:
            return "C"
        elif percentage >= 35 and percentage < 40:
            return "D"
        else:
            return "F (Failed)" 
        
    def get_remarks(self):
        if self.student_data.empty:
            return "N/A"
        
    
        grade = self.get_grade()

        if grade == 'A+':
            return "Outstanding. Keep it up!"
        elif grade == 'A':
            return "Excellent. You can achieve more with a bit of extra work." 
        elif grade == 'B+':
            return "Very Good"
        elif grade == 'B':
            return "Good. You can put in more efforts."
        elif grade == 'C+':
            return "Above Average. Your efforts are not bad, do more hark work."
        elif grade == 'C':
            return "Average. You can get more marks by adding more time and efforts."
        elif grade == 'D':
            return "Below Average. Seems that you are not giving priority to studies."
        else:
            return "You have failed the exam. You are being careless. So, make a routine, don't waste time and make studies your priority. (Extra classes are organized for you.)"
        
         
# --- Main execution ---

# 1. Create a pandas DataFrame from the dictionary
data = pd.DataFrame(dataframe)
print("Original DataFrame:")
print(data)

# 2. Create an object (an instance) of the Result class
result_object = Result(data)

# 3. Call the average_marks() method on the object and store the result
average_marks_per_subject = result_object.average_marks()
highest_marks = result_object.maximum_marks()
lowest_marks = result_object.miminum_marks()

# 4. Print the computed average marks
print("\nAverage marks per subject:")
print(average_marks_per_subject)
print("\nHighest Marks is:")
print(highest_marks)
print("\nLowest Marks is:")
print(lowest_marks)

# Loop to check multiple students
while True:
    print("\n" + "="*50)
    # Get user input for the student's name
    student_to_find = input("Enter the name of the student to report on: ")
    
    # Create an instance of the class using the user's input
    student_report = StudentReport(data, student_to_find)
    
    # Display the results only if student was found
    if not student_report.student_data.empty:
        print(f"\nPercentage for {student_to_find}: {student_report.get_percentage():.2f}%")
        print(f"Grade for {student_to_find}: {student_report.get_grade()}")
        print(f"Remarks: {student_report.get_remarks()}")
    
    # Ask if user wants to continue
    print("\n" + "-"*50)
    choice = input("Do you want to continue (1) or exit (0)? ")
    
    if choice == '0':
        print("\nThank you for using the Student Result Management System!")
        break
    elif choice == '1':
        continue
    else:
        print("Invalid input. Exiting the program.")
        break