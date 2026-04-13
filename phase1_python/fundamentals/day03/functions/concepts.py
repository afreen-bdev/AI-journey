# Function Concepts

# Simple function
def greet():
    print("Hello, welcome!")

greet()

# Function with parameters
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# Function with multiple operations
def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

calculator(10, 2)

# Function with return
def square(num):
    return num * num

print("Square:", square(4))

# Scope example
x = 10

def show():
    x = 5
    print("Local x:", x)

show()
print("Global x:", x)