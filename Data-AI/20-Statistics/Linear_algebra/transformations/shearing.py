import numpy as np

k = 2

A = np.array([
    [1, k],
    [0, 1]
])

v = np.array([1,2])

sheared = A @ v

print("Shearing:")
print("Original:", v)
print("Sheared:", sheared)