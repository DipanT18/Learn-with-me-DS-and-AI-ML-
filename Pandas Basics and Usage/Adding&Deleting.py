#This program is written to demonstrate various methods of adding, modifying and deleting data in a pandas DataFrame.

import pandas as pd

data = {
    'Name': ['Dipan', 'Manjil', 'Samar', 'Rohan', 'Brook', 'Goldie', 'Lucy'],
    'Age': [23, 25, 22, 24, 26, 27, 21],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio'],
    'Profession': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Scientist', 'Teacher', 'Nurse']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

print("-" * 50)
print("Adding, Modifying and Deleting Data...")
print("-" * 50)

#Adding a new column
df['Salary'] = [70000, 120000, 50000, 90000, 110000, 60000, 45000]
print("DataFrame after adding 'Salary' column:\n", df)

#Modifying an existing column
df['Age'] = df['Age'] + 1
print("DataFrame after incrementing 'Age' by 1:\n", df)

#Deleting a column
df.drop('City', axis=1, inplace=True)
print("DataFrame after deleting 'City' column:\n", df)

#Adding a new row
new_row = {'Name': 'Alice', 'Age': 28, 'Profession': 'Designer', 'Salary': 75000}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("DataFrame after adding a new row:\n", df)

#Modify based on condition
df.loc[df['Name'] == 'Rohan', ['Salary']] = 95000
print("DataFrame after modifying 'Salary' for Rohan:\n", df)

#Deleting a row
df.drop(df[df['Name'] == 'Lucy'].index, inplace=True)
print("DataFrame after deleting the row where Name is 'Lucy':\n", df)

