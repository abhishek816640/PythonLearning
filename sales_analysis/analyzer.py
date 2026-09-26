import pandas as pd
from helpers import calculate_total , format_currency

#Read data
df = pd.read_csv('data/sales.csv')

#calculate total of each row
totals = []
for index , row in df.iterrows():
    total = calculate_total(row['quantity'],row['price'])
    totals.append(total)
print(totals)

#Add totals to our data
df['total'] = totals

#display with formatted totals
print("Sales data:")
for index,row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']} : {formatted_total}")

#show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)   
print(f"\nGrant Total is : {formatted_grand_total}")