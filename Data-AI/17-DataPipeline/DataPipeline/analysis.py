import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# 1. Total sales
cursor.execute("SELECT SUM(sales) FROM sales")
print("Total Sales:", cursor.fetchone()[0])

# 2. Sales by region
cursor.execute("""
SELECT region, SUM(sales)
FROM sales
GROUP BY region
""")
print("\nSales by Region:")
for row in cursor.fetchall():
    print(row)

# 3. Top performer
cursor.execute("""
SELECT name, MAX(sales)
FROM sales
""")
print("\nTop Performer:", cursor.fetchone())

conn.close()