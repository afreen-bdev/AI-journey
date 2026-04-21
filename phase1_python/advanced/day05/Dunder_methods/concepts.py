class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return f"{self.name} scored {self.marks}"
    def __len__(self):
        return self.marks
s = Student("Afreen",90)

print(s)
print(len(s))

#operator overloading

class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)

print("Addition:",n1+n2)