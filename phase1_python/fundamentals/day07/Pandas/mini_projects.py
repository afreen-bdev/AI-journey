# Sales Data Analysis (Pandas)

import pandas as pd

# Sample data
data = {
    "product": ["A", "B", "A", "C", "B"],
    "sales": [100, 200, 150, 300, 250],
    "region": ["East", "West", "East", "South", "West"]
}

df = pd.DataFrame(data)

print("Full Data:\n", df)

# Total sales
print("\nTotal Sales:", df["sales"].sum())

# Average sales
print("Average Sales:", df["sales"].mean())

# Group by product
print("\nSales by Product:\n", df.groupby("product")["sales"].sum())

# Group by region
print("\nSales by Region:\n", df.groupby("region")["sales"].sum())

# Top sale
print("\nHighest Sale:\n", df.loc[df["sales"].idxmax()])