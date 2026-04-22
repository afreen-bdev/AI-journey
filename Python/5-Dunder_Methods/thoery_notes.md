# Dunder (Magic) Methods

## 1. What are Dunder Methods?

Special methods in Python that start and end with __

Example:
__init__, __str__, __add__

---

## 2. Why Use Them?

- Customize object behavior
- Make objects behave like built-in types

---

## 3. Common Dunder Methods

__init__ → constructor  
__str__ → user-friendly print  
__repr__ → developer representation  
__len__ → length  
__add__ → + operator  

---

## 4. __str__ vs __repr__

__str__ → readable output  
__repr__ → detailed/debug output  

---

## 5. Operator Overloading

Allows operators to work with custom objects

Example:
obj1 + obj2

---

## 6. Real Use Cases

- Custom data models
- ML objects
- Framework design

---

## Key Takeaways

- Dunder methods = powerful customization
- Makes your classes more Pythonic

# File Handling in Python

## 1. Why File Handling?

- Store data permanently
- Read existing data
- Used in real-world systems (logs, datasets, configs)

---

## 2. Opening a File

open("file.txt", mode)

Modes:
'r' → read  
'w' → write (overwrite)  
'a' → append  
'x' → create  

---

## 3. Reading File

file.read()
file.readline()
file.readlines()

---

## 4. Writing File

file.write("text")

---

## 5. Closing File

file.close()

---

## 6. Best Practice (IMPORTANT)

Use with statement:
with open("file.txt", "r") as file:
    data = file.read()

👉 Automatically closes file

---

## 7. File Handling Flow

Open → Read/Write → Close

---

## Key Takeaways

- Files store persistent data
- Always use 'with open'
- Important for ML datasets & logs

# Exception Handling in Python

## 1. What is Exception?

An exception is an error that occurs during program execution.

Example:
10 / 0 → ZeroDivisionError

---

## 2. Why Exception Handling?

- Prevent program crash
- Handle errors gracefully
- Improve user experience

---

## 3. try-except

try:
    code
except:
    handle error

---

## 4. Specific Exceptions

except ZeroDivisionError:
except ValueError:

---

## 5. try-except-else-finally

try:
    code
except:
    handle error
else:
    runs if no error
finally:
    always runs

---

## 6. Raising Exception

raise ValueError("Invalid input")

---

## 7. Best Practices

- Catch specific exceptions
- Avoid bare except
- Use finally for cleanup

---

## Key Takeaways

- Exceptions make programs safe
- Required in real applications

# Modules & Packages

## 1. What is a Module?

A module is a Python file (.py) containing functions/variables.

Example:
utils.py

---

## 2. Why Modules?

- Code organization
- Reusability
- Clean structure

---

## 3. Importing Modules

import module_name

from module_name import function

---

## 4. __name__ == "__main__"

Used to check if file is run directly

---

## 5. What is a Package?

A folder containing multiple modules

Example:
project/
   utils.py
   main.py

---

## 6. Benefits

- Modular code
- Easy maintenance
- Scalable systems

---

## Key Takeaways

- Modules = single file reuse
- Packages = structured project
- Essential for real-world apps