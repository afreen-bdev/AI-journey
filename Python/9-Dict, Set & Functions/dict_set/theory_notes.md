# Day 05 — Dictionary & Set

## 1. Dictionary

A dictionary stores data in key-value pairs.

Example:
student = {"name": "Afreen", "age": 22}

---

## 2. Properties

- Unordered (Python 3.7+ keeps insertion order)
- Mutable
- Keys must be unique

---

## 3. Accessing Data

student["name"]

---

## 4. Adding / Updating

student["marks"] = 90

---

## 5. Removing

del student["age"]
student.pop("marks")

---

## 6. Iteration

for key, value in student.items():
    print(key, value)

---

## 7. Set

A set:
- Unordered
- Unique elements only
- Mutable

Example:
nums = {1, 2, 3}

---

## 8. Set Operations

add(), remove()

---

## 9. Use Cases

Dictionary → structured data (APIs, ML records)  
Set → remove duplicates, fast lookup  

---

## Key Takeaways

- Dict = real-world data modeling  
- Set = uniqueness + performance  