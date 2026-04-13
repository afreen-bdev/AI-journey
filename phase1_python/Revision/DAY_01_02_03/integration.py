# Practice — Combine Concepts
# Store students
students = []

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    student = {"name": name, "marks": marks}
    students.append(student)


def show_students():
    if not students:
        print("No students found")
        return

    for s in students:
        print(s["name"], "-", s["marks"])


def find_topper():
    if not students:
        print("No data")
        return

    topper = students[0]

    for s in students:
        if s["marks"] > topper["marks"]:
            topper = s

    print("Topper:", topper["name"], topper["marks"])


# Menu system
while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        show_students()
    elif choice == 3:
        find_topper()
    elif choice == 4:
        break
    else:
        print("Invalid choice")