#This is the first program written to demonstrate the creation of a dataframe using pandas library
 
'''What is a DataFrame?
A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). It is one of the most commonly used data structures in the pandas library for data manipulation and analysis. DataFrames allow you to store and manipulate data in a way that is similar to a spreadsheet or SQL table, making it easy to perform operations such as filtering, grouping, and aggregating data.'''

import pandas as pd

data = {
    'Name': ['Dipan', 'Manjil', 'Samar', 'Rohan', 'Brook', 'Goldie', 'Lucy'],
    'Age': [23, 25, 22, 24, 26, 27, 21],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio'],
    'Profession': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Scientist', 'Teacher', 'Nurse']
}

df = pd.DataFrame(data)
#First dataframe
print(df)
print("\n Type of df:", type(df))

#Properties of dataframe
print("\n DataFrame Info:")
print(df.info())
print("\n DataFrame Description:")
print(df.describe(include='all'))
print("\n DataFrame Shape:", df.shape)
print("\n DataFrame Columns:", df.columns.tolist())
print("\n DataFrame Index:", df.index.tolist())
print("\n DataFrame Dtypes:\n", df.dtypes)
print("\n DataFrame Head:\n", df.head())
print("\n DataFrame Tail:\n", df.tail())


#Intro to series
name = df['Name']
print("\n Series (Name Column):\n", name)
print("\n Type of name:", type(name))

#Creating dataframe from different data structures

#From list of lists
data_list = [
    ['Alice', 30, 'New York', 'Engineer'],
    ['Bob', 28, 'Los Angeles', 'Doctor'],
    ['Charlie', 35, 'Chicago', 'Artist']
]
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City', 'Profession'])
print("\n DataFrame from List of Lists:\n", df_from_list)

#From list of dictionaries
data_list_of_dicts = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York', 'Profession': 'Engineer'},
    {'Name': 'Bob', 'Age': 28, 'City': 'Los Angeles', 'Profession': 'Doctor'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago', 'Profession': 'Artist'}
]
df_from_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print("\n DataFrame from List of Dictionaries:\n", df_from_list_of_dicts)  

#From dictionary of lists
data_dict_of_lists = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Profession': ['Engineer', 'Doctor', 'Artist']
}
df_from_dict_of_lists = pd.DataFrame(data_dict_of_lists)
print("\n DataFrame from Dictionary of Lists:\n", df_from_dict_of_lists)

#From dictionary of dictionaries
data_dict_of_dicts = {
    'row1': {'Name': 'Alice', 'Age': 30, 'City': 'New York', 'Profession': 'Engineer'},
    'row2': {'Name': 'Bob', 'Age': 28, 'City': 'Los Angeles', 'Profession': 'Doctor'},
    'row3': {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago', 'Profession': 'Artist'}
}
df_from_dict_of_dicts = pd.DataFrame.from_dict(data_dict_of_dicts, orient='index')
print("\n DataFrame from Dictionary of Dictionaries:\n", df_from_dict_of_dicts)