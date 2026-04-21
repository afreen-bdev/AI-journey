import pandas as pd

data = {
    "name" : ["A","B","C"],
    "marks" : [85,90,78],
    "age" : [20,21,19]
}

df = pd.DataFrame(data)

print("DataFrame:\n",df)

print("\nHead:\n",df.head())
print("\nInfo:")
print(df.info())

print("\nMarks column:\n",df["marks"])

# Multiple columns
print("\nName & Age:\n", df[["name", "age"]])

# Filtering
print("\nMarks > 80:\n", df[df["marks"] > 80])

# Add new column
df["status"] = ["Pass", "Pass", "Pass"]
print("\nAfter adding column:\n", df)

# Sorting
print("\nSorted by marks:\n", df.sort_values(by="marks", ascending=False))