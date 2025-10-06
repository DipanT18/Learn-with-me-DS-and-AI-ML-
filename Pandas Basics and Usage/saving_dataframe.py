#This code demonstrates how to save a pandas DataFrame to different file formats such as CSV, Excel, and JSON.

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
print("Saving DataFrame to CSV, Excel, and JSON formats...")
print("-" * 50)

# Save DataFrame to CSV
df.to_csv('data.csv', index=False)
print("DataFrame saved to data.csv")

# Save DataFrame to Excel
try:
    import openpyxl
    df.to_excel('data.xlsx', index=False)
    print("DataFrame saved to data.xlsx")
except ImportError:
    print("openpyxl is not installed. DataFrame not saved to Excel.")

# Save DataFrame to JSON
try:
    import json
    df.to_json('data.json', orient='records', lines=True)
    print("DataFrame saved to data.json")
except ImportError:
    print("json is not installed. DataFrame not saved to JSON.")

#Now reading the data
print("-" * 50)
print("Reading the saved files back into DataFrames...")    
print("-" * 50)

# Read DataFrame from CSV
df_csv = pd.read_csv('data.csv')
print("DataFrame read from data.csv:\n", df_csv)

# Read DataFrame from Excel
try:
    df_excel = pd.read_excel('data.xlsx')
    print("DataFrame read from data.xlsx:\n", df_excel)
except ImportError:
    print("openpyxl is not installed. DataFrame not read from Excel.")

# Read DataFrame from JSON
try:
    df_json = pd.read_json('data.json', orient='records', lines=True)
    print("DataFrame read from data.json:\n", df_json)
except ImportError:
    print("json is not installed. DataFrame not read from JSON.")
