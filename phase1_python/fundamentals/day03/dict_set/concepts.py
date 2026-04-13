# Dictionary creation
student = {
    "name" : "Afreen",
    "age" : 22,
    "marks" : 85
}
print ("Student:",student)

# Access
print("Name:",student["name"])

# Add / Update
student["marks"]=90
student["city"]="Vizag"

print("updated:",student)

# Remove
student.pop("age")
print("after removal:",student)

# Iteration
print("\nIterating dictionary:")
for key, value in student.items():
    print(key,":", value)

# Set creation
numbers = {1,2,3,2,1}
print("\nSet(unique values):",numbers)

#add element
numbers.add(4)
print("After adding:",numbers)

# remove element
numbers.remove(2)
print("after removing:",numbers)