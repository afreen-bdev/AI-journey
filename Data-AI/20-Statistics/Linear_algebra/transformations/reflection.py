import numpy as np

# Reflection across Y-axis
A = np.array([
    [-1, 0],
    [0, 1]
])

v = np.array([3,4])

reflected = A @ v

print("Reflection:")
print("Original:", v)
print("Reflected:", reflected)