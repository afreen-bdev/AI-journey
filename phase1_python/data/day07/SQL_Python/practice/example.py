import sqlite3

conn = sqlite3.connect("practice.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    amount INTEGER
)
""")

# Insert data
data = [("A", 100), ("B", 200), ("A", 150)]
cursor.executemany("INSERT INTO sales VALUES (?, ?)", data)

conn.commit()

# 1. Total sales
cursor.execute("SELECT SUM(amount) FROM sales")
print("Total Sales:", cursor.fetchone())

# 2. Group by product
cursor.execute("SELECT product, SUM(amount) FROM sales GROUP BY product")
print("Sales by product:", cursor.fetchall())

conn.close()