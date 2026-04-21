try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid number")
