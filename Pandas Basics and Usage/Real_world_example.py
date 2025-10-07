#This program is written to demonstrate a real-world example of data analysis using pandas library in Python.
#This is predicting the customer churn for a telecom company.

import pandas as pd
import numpy as np


# Sample dataset creation
customer_data = pd.DataFrame({
    'CustomerID': range(1, 11),
    'Age': np.random.randint(18, 70, 10),
    'Tenure': np.random.randint(1, 72, 10),  # in months
    'MonthlyCharges': np.random.uniform(20.0, 120.0, 10).round(2),
    'TotalCharges': np.random.uniform(100.0, 8000.0, 10).round(2),
    'Churn': np.random.choice(['Yes', 'No'], 10, p=[0.3, 0.7])
})

print("Customer Data:")
print(customer_data)

#Simple Analysis
print(f"Dataset Information:\n{customer_data.info()}")
print(f"Descriptive Statistics:\n{customer_data.describe()}")
print(f"Churn Distribution:\n{customer_data['Churn'].value_counts(normalize=True)}")

#Data Cleaning
# Check for missing values
print(f"Missing Values:\n{customer_data.isnull().sum()}")


#Checking for duplicates
duplicates = customer_data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Remove duplicates if any
if duplicates > 0:
    customer_data = customer_data.drop_duplicates()
    print("Duplicates removed.")
    print(f"New shape of data: {customer_data.shape}")

#Feature Engineering
customer_data['AvgMonthlyCharges'] = customer_data['TotalCharges'] / customer_data['Tenure']
customer_data['Most_Expensive'] = customer_data['MonthlyCharges'] > customer_data['MonthlyCharges'].mean()
customer_data['Age_Group'] = pd.cut(customer_data['Age'], bins=[17, 28, 45, 60, 100], labels=['GenZ', 'Youth', 'Adult', 'Senior'])
print("Feature Engineering Completed.")
print(customer_data)


#Data Analysis by grouping
print(f"Churned Customers by Age Group:\n{customer_data.groupby('Age_Group')['Churn'].value_counts(normalize=True)}")

print(f"Average Monthly Charges by Churn Status:\n{customer_data.groupby('Churn')['MonthlyCharges'].mean()}")

features = ['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges', 'AvgMonthlyCharges']
X = customer_data[features]
Y = customer_data['Churn']
print("Features and target variable separated.")
print(f"Features:\n{X.shape}")
print(f"Target Variable:\n{Y.shape}")