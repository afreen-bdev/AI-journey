# Mini Project — Student Database System

import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Topper")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
        conn.commit()
        print("Student added")

    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)

    elif choice == 3:
        cursor.execute("SELECT name, MAX(marks) FROM students")
        print("Topper:", cursor.fetchone())

    elif choice == 4:
        break

conn.close()