#This program is written to clean data , handle missing values and duplicates in a dataset using pandas library in Python.

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve', 'Frank', 'Alice'],
    'Age': [25, 30, None, 22, 28, None, 25],
    'City': ['New York', None, 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'New York'],
    'Income': [70000, 80000, 120000, None, 95000, 60000, 70000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Detecting missing values
print("\nMissing values in each column:")
print(df.isnull())

print("\nCount of missing values in each column:")
print(df.isnull().sum())

print(f"\nTotal missing values in DataFrame: {df.isnull().sum().sum()}")

# Handling missing values
print("\nDataFrame after dropping rows with any missing values:")
df_dropped = df.dropna()
print(df_dropped)

print("\n Removing rows where all elements are missing:")
df_dropped_all = df.dropna(how='all')
print(df_dropped_all)

print ("\n Removing columns with any missing values:")
df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols)

# Filling missing values with a specific value
print("\nDataFrame after filling missing values with 0:")
df_filled = df.fillna(0)
print(df_filled)

# Filling missing values with the mean of the column
print("\nDataFrame after filling missing values in 'Age' with the mean:")
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

print("\n Filling Dataframes with forward fill method:")
df_ffill = df.fillna(method='ffill')
print(df_ffill)

print("\n Filling Dataframes with backward fill method:")
df_bfill = df.fillna(method='bfill')
print(df_bfill)


# Handling duplicates
print("\nDataFrame after removing duplicate rows:")
df_dropped_duplicates = df.drop_duplicates()
print(df_dropped_duplicates)