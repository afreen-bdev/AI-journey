# Mini Project — Number Analyzer Tool
print("---- Number Analyzer ----")
num = int(input("Enter a number: "))
# Even / Odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Factorial
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
# Sum of digits
temp = num
sum_digits = 0
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("Sum of digits:", sum_digits)