# Day 02 — Control Flow in Python

## 1. What is Control Flow?
Control flow determines how your program makes decisions.

---

## 2. if Statement

Syntax:
if condition:
    code

Example:
age = 18

if age >= 18:
    print("Eligible to vote")

---

## 3. if-else

if condition:
    code
else:
    code

---

## 4. if-elif-else

if condition1:
    code
elif condition2:
    code
else:
    code

---

## 5. Nested if

if condition:
    if another_condition:
        code

---

## 6. Comparison Operators

==  Equal  
!=  Not equal  
>   Greater than  
<   Less than  
>=  Greater or equal  
<=  Less or equal  

---

## 7. Logical Operators

and → both true  
or → at least one true  
not → reverse condition  

---

## 8. Important Concepts

- Indentation is mandatory
- Conditions must return True/False
- Avoid too many nested ifs

---

## Key Takeaways

- Control flow = decision making
- Combine conditions for real-world logic

## Loops in Python

## 1. What are Loops?
Loops are used to repeat a block of code multiple times.

---

## 2. for Loop

Used when number of iterations is known.

Syntax:
for variable in range():
    code

Example:
for i in range(5):
    print(i)

---

## 3. range() Function

range(start, end, step)

Example:
range(1, 10, 2)

---

## 4. while Loop

Used when condition-based repetition is needed.

Syntax:
while condition:
    code

---

## 5. Loop Control Statements

break → stops loop  
continue → skips current iteration  

---

## 6. Nested Loops

Loop inside another loop

Example:
for i in range(3):
    for j in range(3):
        print(i, j)

---

## 7. When to Use What?

for → fixed iterations  
while → condition-based  

---

## Key Takeaways

- Loops help automate tasks
- Avoid infinite loops
- Use break/continue carefully