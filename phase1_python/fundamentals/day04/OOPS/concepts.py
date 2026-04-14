# class Student:

#     def __init__(self, name, age):
#         self.name= name
#         self.age=age

#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)

# s1 = Student("Afreen", 23)
# s1.display()

class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price=price

    def show(self):
        print(self.brand,"-",self.price)

car1 = Car("Toyota", 100000)
car1.show()
        
