# Modular Student System
# utils_student.py logic inside same file for simplicity

def add_student(students):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})


def show_students(students):
    for s in students:
        print(s["name"], "-", s["marks"])


students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student(students)
    elif choice == 2:
        show_students(students)
    elif choice == 3:
        break