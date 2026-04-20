import pandas as pd

data = {
    "product": ["A", "B", "C", "A", "B", "C"],
    "sales": [100, 200, None, 150, 250, 300],
    "region": ["East", "West", "East", "South", "West", None]
}

df = pd.DataFrame(data)

#Handle missing values
df["sales"].fillna(df["sales"].mean(), inplace=True)
df["region"].fillna("Unknown", inplace=True)

# Remove duplicates
df = df.drop_duplicates()

#Add new column
df["sales_category"] = df["sales"].apply(
    lambda x: "High" if x > 200 else "Low"
)

#Group analysis
print("\nSales by region:\n", df.groupby("region")["sales"].sum())

#Sort
print("\nSorted:\n", df.sort_values(by="sales", ascending=False))