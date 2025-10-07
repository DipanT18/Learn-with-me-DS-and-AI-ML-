#This program demonstrates how to merge and join DataFrames using pandas library in Python.

import pandas as pd

# Creating two sample DataFrames
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}
data2 = {
    'ID': [1, 2, 3, 4],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Income': [70000, 80000, 120000, 90000]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

#Merging DataFrames on a common column 'ID'
merged_df = pd.merge(df1, df2, on='ID')
print("\nMerged DataFrame on 'ID':")
print(merged_df)

#Left Join
left_join_df = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join DataFrame:")
print(left_join_df)

#Right Join
right_join_df = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join DataFrame:")
print(right_join_df)

#Concat DataFrames
concat_df = pd.concat([df1, df2], axis=0)
print("\nConcatenated DataFrame (axis=0):")
print(concat_df)
concat_df_axis1 = pd.concat([df1, df2], axis=1)
print("\nConcatenated DataFrame (axis=1):")
print(concat_df_axis1)

