# Employee Management System

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, "| Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        print(self.name, "| Salary:", self.salary, "| Team:", self.team_size)


employees = []

print("---- Employee System ----")

for i in range(2):
    role = input("Enter role (manager/employee): ").lower()
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    if role == "manager":
        team = int(input("Enter team size: "))
        emp = Manager(name, salary, team)
    else:
        emp = Employee(name, salary)

    employees.append(emp)


print("\n--- Employee List ---")

for emp in employees:
    emp.display()