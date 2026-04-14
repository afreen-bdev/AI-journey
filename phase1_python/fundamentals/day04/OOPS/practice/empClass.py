class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name,self.salary)

e1 = Employee("John",50000)
e1.show()