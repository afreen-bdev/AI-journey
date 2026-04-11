# Mini Project — Student Marks Manager
students = []
print("---- Student Marks Manager ----")
for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append((name, marks))  # tuple inside list

print("\n--- Student Records ---")
for student in students:
    print("Name:", student[0], "| Marks:", student[1])

# Find topper
topper = students[0]
for student in students:
    if student[1] > topper[1]:
        topper = student

print("\nTopper:", topper[0], "with", topper[1], "marks")