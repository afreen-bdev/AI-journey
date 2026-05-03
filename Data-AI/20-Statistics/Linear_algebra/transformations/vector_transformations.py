import numpy as np

# Transformation matrix
A = np.array([
    [1, 1, 0],
    [0, 0, 2]
])

x = np.array([1,2,3])

print("Vector Transformation:")
print("Input:", x)
print("Output:", A @ x)