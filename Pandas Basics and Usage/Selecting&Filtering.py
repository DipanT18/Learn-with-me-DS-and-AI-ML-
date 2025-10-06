#This program is written to demonstrate various methods of selecting and filtering data in a pandas DataFrame.

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
print("Selecting and Filtering Data...")
print("-" * 50)

#Selecting a single column
print("Selecting the 'Name' column:\n", df['Name'])
'''OR'''
print("Selecting the 'Age' column:\n", df['Age'])

#Selecting multiple columns
print("Selecting 'Name' and 'City' columns:\n", df[['Name', 'City']])

#Filtering rows based on a condition
print("Filtering rows where Age > 24:\n", df[df['Age'] > 24])
print("Filtering rows where City is 'Chicago':\n", df[df['City'] == 'Chicago'])

#Using loc to select rows and columns by labels
#Loc is defined as label based indexing
print(f"First row using loc:\n{df.loc[0]}")
print(f"Rows 1 to 3 and columns 'Name' and 'Age' using loc:\n{df.loc[1:3, ['Name', 'Age']]}")
print(f"All rows and 'City' column using loc:\n{df.loc[:, 'City']}")

#Using iloc to select rows and columns by integer position
#Iloc is defined as integer position based indexing
print(f"First row using iloc:\n{df.iloc[0]}")
print(f"Rows 1 to 3 and columns 0 and 1 using iloc:\n{df.iloc[1:3, [0, 1]]}")
print(f"All rows and 'City' column using iloc:\n{df.iloc[:, 2]}")

#Filtering with multiple conditions
print("Filtering rows where Age > 22 and City is 'New York':\n", df[(df['Age'] > 22) & (df['City'] == 'New York')])
print("Filtering rows where Age < 25 or Profession is 'Teacher':\n", df[(df['Age'] < 25) | (df['Profession'] == 'Teacher')])

#Using string based filtering
print("Filtering rows where Name starts with 'D':\n", df[df['Name'].str.startswith('D')])

#Using isin for filtering
print("Filtering rows where City is either 'Chicago' or 'Houston':\n", df[df['City'].isin(['Chicago', 'Houston'])])

#Using 'And' and 'Or' operators for filtering
print("Filtering rows where Age > 22 and Profession is 'Engineer':\n", df[(df['Age'] > 22) & (df['Profession'] == 'Engineer')])
print("Filtering rows where Age < 23 or City is 'Phoenix':\n", df[(df['Age'] < 23) | (df['City'] == 'Phoenix')])

#Between method for filtering
print("Filtering rows where Age is between 22 and 25:\n", df[df['Age'].between(22, 25)])

#Using query method for filtering
print("Filtering rows using query method where Age > 24:\n", df.query('Age > 24'))
print("Filtering rows using query method where City == 'Chicago':\n", df.query("City == 'Chicago'"))