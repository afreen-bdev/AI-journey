# Mini Project — Robust Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print("---- Robust Calculator ----")

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = int(input("Choose option: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        elif choice == 5:
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid numbers only")