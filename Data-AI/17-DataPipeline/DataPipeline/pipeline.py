import pandas as pd
import sqlite3
import os

print("Current directory:", os.getcwd())
print("Files:", os.listdir())
# Load CSV
df = pd.read_csv("phase1_python/fundamentals/day08/DataPipeline/data.csv")

print("Original Data:\n",df)

# data cleaning
df["age"].fillna(df["age"].median(),inplace=True)
df["sales"].fillna(df["sales"].mean(),inplace=True)

print("\nCleaned Data:\n",df)

# transformation
df["sales_category"] = df["sales"].apply(
    lambda x : "High" if x>200 else "Low"
)

# store in SQL
conn = sqlite3.connect("sales.db")
df.to_sql("sales",conn,if_exists="replace",index=False)

print("\nData stored in database")

conn.close()