# Day 08 — OOP Basics (Classes & Objects)

## 1. What is OOP?

Object-Oriented Programming is a way to structure code using:
- Classes
- Objects

---

## 2. Class

A class is a blueprint.

Example:
class Student:
    pass

---

## 3. Object

An object is an instance of a class.

Example:
s1 = Student()

---

## 4. __init__ Method

Constructor → initializes object

Example:
class Student:
    def __init__(self, name):
        self.name = name

---

## 5. self Keyword

- Refers to current object
- Used to access variables

---

## 6. Attributes & Methods

Attributes → variables inside class  
Methods → functions inside class  

---

## 7. Why OOP?

- Organizes code
- Reusability
- Real-world modeling

---

## Key Takeaways

- Class = structure
- Object = actual data
- OOP is used everywhere (backend, ML models)

# Day 09 — Inheritance & Polymorphism

## 1. What is Inheritance?

Inheritance allows one class to use properties of another class.

Example:
class Parent:
    pass

class Child(Parent):
    pass

---

## 2. Why Inheritance?

- Code reuse
- Avoid duplication
- Logical hierarchy

---

## 3. Types (Basic)

- Single inheritance
- Multilevel inheritance

---

## 4. Method Overriding

Child class can redefine parent method.

---

## 5. super() Keyword

Used to call parent constructor

Example:
super().__init__()

---

## 6. Polymorphism

Same method name → different behavior

Example:
Different classes with same method name

---

## 7. Real-World Example

Vehicle → Car, Bike  
Employee → Manager, Developer  

---

## Key Takeaways

- Inheritance = reuse
- Polymorphism = flexibility
- Important for large systems