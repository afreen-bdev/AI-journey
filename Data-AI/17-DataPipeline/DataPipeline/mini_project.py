import pandas as pd
import sqlite3

print("---- Advanced Data Pipeline ----")

# Load data
df = pd.read_csv("phase1_python/fundamentals/day08/DataPipeline/data.csv")

# Cleaning
df.fillna({
    "age": df["age"].median(),
    "sales": df["sales"].mean()
}, inplace=True)

# Feature Engineering
df["performance"] = df["sales"].apply(
    lambda x: "Top" if x > 200 else "Normal"
)

# Store in DB
conn = sqlite3.connect("pipeline.db")
df.to_sql("data", conn, if_exists="replace", index=False)

# Analysis
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM data")
total = cursor.fetchone()[0]

cursor.execute("SELECT region, SUM(sales) FROM data GROUP BY region")
region_data = cursor.fetchall()

print("\nTotal Records:", total)
print("\nSales by Region:")
for row in region_data:
    print(row)

conn.close()