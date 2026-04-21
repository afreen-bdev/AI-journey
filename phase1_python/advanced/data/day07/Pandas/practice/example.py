import pandas as pd

data = {
    "name" : ["A","B","C","D"],
    "marks" : [85, 90, None, 70],
    "age" : [20, 21, 22, 19]
}

df = pd.DataFrame(data)

print("\nMissing values:\n",df.isnull())

df["marks"].fillna(df["marks"].mean(),inplace=True)

def grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"
df["grade"] = df["marks"].apply(grade)

top_students = df[df["marks"]>80]

print("\nTop Students:\n",top_students)

print("\nAverage age by grade:\n", df.groupby("grade")["age"].mean())