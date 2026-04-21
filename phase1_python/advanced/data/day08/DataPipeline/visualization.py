import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("sales.db")
df = pd.read_sql("SELECT * FROM sales",conn)

print(df)

# sales by region(bar chart)
region_sales = df.groupby("region")["sales"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("sales by region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# sales distribution(histogram)
plt.figure()
plt.hist(df["sales"])
plt.title("sales distribution")
plt.xlabel("sales")
plt.ylabel("frequency")
plt.show()

# boxplot(outliers detection)
plt.figure()
sns.boxplot(x=df["sales"])
plt.title("Sales outliers")
plt.show()

conn.close()