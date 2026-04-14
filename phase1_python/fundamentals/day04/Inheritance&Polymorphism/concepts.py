# inheritance
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print("name:",self.name)
# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks
#     def show(self):
#         print("name:",self.name,"|Mrks:",self.marks)
# s = Student("afreen",90)
# s.show()

# polymorphism
class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")
def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())