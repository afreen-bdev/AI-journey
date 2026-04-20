import utils

print("---- Modular Calculator ----")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Add:", utils.add(a, b))
print("Subtract:", utils.subtract(a, b))
print("Multiply:", utils.multiply(a, b))
print("Divide:", utils.divide(a, b))