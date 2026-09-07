import os
import pandas as pd
import json

#Check which directory we are in
print("Current directory : ",os.getcwd())

#Check if our data file exists
data_path = "data/sales.csv"
#data_path = "..data/analyzer.py"
if os.path.exists(data_path):
    print("The file has been found")
else:
    print(f"Cannot find {data_path}")
    print("make Sure you are running from sales-analysis")    

#Read the csv file
df = pd.read_csv('data/sales.csv')
print("CSV Data :")
print(df)
print(f"\nShape : {df.shape[0]} rows,{df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print(f"\nWith Totals : ")
print(df)

#Create output directory
os.makedirs('output',exist_ok=True)

# Save as different formats
# 1. Excel format (good for sharing)
df.to_excel('output/sales_data.xlxs', index=False)



