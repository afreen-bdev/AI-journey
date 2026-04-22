#Student Class System (OOP)
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"{self.name} | Age: {self.age} | Marks: {self.marks}")


students = []

print("---- Student System (OOP) ----")

for i in range(3):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    student = Student(name, age, marks)
    students.append(student)

print("\n--- Student List ---")

for s in students:
    s.display()