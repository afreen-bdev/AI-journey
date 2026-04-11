print("---- Student Grade System ----")

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n----- RESULT -----")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("------------------")

# Additional logic
if marks >= 50:
    print("Status: Passed")
else:
    print("Status: Failed")