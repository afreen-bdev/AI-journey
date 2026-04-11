# Day 02 — Lists & Tuples Concepts
# List creation
numbers = [1,2,3,4,5]
print("List:",numbers)

# Access elements
print("first element:",numbers[0])

# Add elements
numbers.append(6)
numbers.insert(1,10)
print("After adding:",numbers)

# Remove elements
numbers.remove(3)
numbers.pop()
print("After removal:", numbers)

# Loop through list
print("\niterating list:")
for num in numbers:
    print(num)

# Slicing
print("\nSlicing:",numbers[1:4])

#tuple
coords = (10,20,30)
print("\nTuple:",coords)
print("first value:", coords[0])

# Tuple unpacking
x,y,z = coords
print("Unpacked:",x,y,z)