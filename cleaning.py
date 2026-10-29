#import libraries
import pandas as pd 

# import data
df = pd.read_excel("raw data.xlsx")

# get info about the data
# print(df.info())
# print(df.head())
# print(df.describe())

# remove duplicates
df = df.drop_duplicates()
print(df)

# fix date column 
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

df = df.dropna(subset=['Order_Date'])
print(df)

# add columns 
df['profit'] = df['Sales'] - df['Cost']
df['year'] = df['Order_Date'].dt.year
df['month'] = df['Order_Date'].dt.month
print(df)

# convert to csv file 
df.to_csv("Sales_cleaned.csv", index=False)
print("Data cleaned and successfully saved ")