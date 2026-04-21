import pandas as pd

data = {
    "name" : ["A","B","C","D","D"],
    "marks" : [85,None,78,90,90],
    "age" : [20,21,None,19,19]
}

df = pd.DataFrame(data)

print("Original data:\n",df)

print("\nMissing values:", df.isnull())

df["marks"].fillna(df["marks"].mean(),inplace=True)
df["age"].fillna(df["age"].median(),inplace=True)

df = df.drop_duplicates()

#Data types
print("\nData Types:\n", df.dtypes)

#Summary statistics
print("\nSummary:\n", df.describe())

#Value counts
print("\nName counts:\n", df["name"].value_counts())

#Grouping
print("\nAverage marks:\n", df.groupby("name")["marks"].mean())

print("\nCleaned Data:\n", df)