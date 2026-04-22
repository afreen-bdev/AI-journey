# Basic try-except
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# try-except-else-finally
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", x)
finally:
    print("Execution completed")

# Raising exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18+")

try:
    check_age(16)
except ValueError as e:
    print(e)