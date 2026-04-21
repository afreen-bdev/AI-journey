#Sales Data Cleaning + EDA

import pandas as pd

import matplotlib.pyplot as plt

data = {
    "product": ["A", "B", "C", "A", "B", "C"],
    "sales": [100, None, 150, 200, 250, None],
    "region": ["East", "West", "East", None, "West", "South"]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Cleaning
df["sales"].fillna(df["sales"].mean(), inplace=True)
df["region"].fillna("Unknown", inplace=True)

# Analysis
print("\nTotal Sales:", df["sales"].sum())
print("Average Sales:", df["sales"].mean())

# Grouping
print("\nSales by Product:\n", df.groupby("product")["sales"].sum())

# Top product
top = df.groupby("product")["sales"].sum().idxmax()
print("\nTop Product:", top)

df["sales"].hist()
plt.show()