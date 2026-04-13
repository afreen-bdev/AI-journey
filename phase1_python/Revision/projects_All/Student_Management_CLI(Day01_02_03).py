# Mini Project — Student Management CLI

students = []

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students available")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"{s['name']} | Age: {s['age']} | Marks: {s['marks']}")


def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print("Found:", s)
            return

    print("Student not found")


def show_topper():
    if not students:
        print("No data")
        return

    topper = students[0]

    for s in students:
        if s["marks"] > topper["marks"]:
            topper = s

    print("Topper:", topper["name"], topper["marks"])


# Main menu
while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Show Topper")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        show_topper()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")