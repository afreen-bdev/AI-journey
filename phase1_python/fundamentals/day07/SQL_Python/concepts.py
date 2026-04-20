import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Afreen", 90))
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("John", 80))

conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("All Data:")
for row in rows:
    print(row)

# Filter query
cursor.execute("SELECT * FROM students WHERE marks > 85")
print("\nHigh scorers:", cursor.fetchall())

# Aggregate
cursor.execute("SELECT AVG(marks) FROM students")
print("\nAverage Marks:", cursor.fetchone())

# Close connection
conn.close()