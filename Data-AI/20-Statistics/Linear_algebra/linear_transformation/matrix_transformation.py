import numpy as np

A = np.array([
    [-1, 0],
    [0, 1]
])

def T(x):
    return A @ x

x = np.array([3,4])

print("Matrix Transformation:")
print("Input:", x)
print("Output:", T(x))