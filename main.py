import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("Sales_cleaned.csv")

print(df)

engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/salesdb')

df.to_sql('sales_data', con=engine, if_exists='replace', index=False)
