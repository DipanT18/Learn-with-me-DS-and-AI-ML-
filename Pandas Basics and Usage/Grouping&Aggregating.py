#This code is written to demonstrate the use of grouping and aggragating datasets or dataframes using pandas library

from tokenize import group
import pandas as pd

df = pd.DataFrame({
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Salary': [50000, 55000, 65000, 68000, 52000, 54000],
    'Experience': [2, 3, 5, 6, 3, 4]
})

print("Company Data:\n")
print(df)

print("\n" + "-"*50)
print("Basic Grouping by Department:")

group1 = df.groupby('Department')['Salary'].mean()
print(f"\n Average Salary by Department:\n{group1}")

group2 = df.groupby('Department')['Experience'].sum()
print(f"\n Total Experience by Department:\n{group2}")

group3 = df.groupby('Department').agg({'Salary': 'max', 'Experience': 'min'})
print(f"\n Max Salary and Min Experience by Department:\n{group3}")

group4 = df.groupby('Department')['Employee'].count()
print(f"\n Total Employees by Department:\n{group4}")

print("\n" + "-"*50)
print("Multi-level Grouping by Department and Experience Level:")

group5 = df.groupby(['Department', 'Experience'])['Salary'].agg(['mean', 'max', 'min', 'count', 'sum', 'std'])
print(f"\n Salary Statistics by Department and Experience Level:\n{group5}")

#Aggregating multiple columns with different functions
group6 = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min', 'count', 'sum', 'std'],
    'Experience': ['mean', 'max', 'min', 'count', 'sum', 'std']
})
print(f"\n Salary and Experience Statistics by Department:\n{group6}")