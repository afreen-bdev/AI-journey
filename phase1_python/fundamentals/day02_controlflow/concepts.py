# Day 02 — Control Flow Concepts

# Basic if
age = 20

if age >= 18:
    print("You are eligible to vote")

# if-else
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Logical operators
salary = 50000
experience = 3

if salary > 40000 and experience >= 2:
    print("Eligible for promotion")

# Nested if
age = 25

if age > 18:
    if age < 60:
        print("Working age group")