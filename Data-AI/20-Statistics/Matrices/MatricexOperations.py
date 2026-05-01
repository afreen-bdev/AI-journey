import numpy as np

# Create Matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Shape
print("\nShape of A:", A.shape)
 
# Addition
print("\nAddition A + B:\n", A + B)

# Subtraction
print("\nSubtraction A - B:\n", A - B)

# Scalar Multiplication
print("\nScalar Multiplication (2 * A):\n", 2 * A)

# Matrix Multiplication
print("\nMatrix Multiplication A @ B:\n", A @ B)

# Transpose
print("\nTranspose of A:\n", A.T)

# Dot Product (Single Row & Column)
row = np.array([1, 2, 3])
col = np.array([4, 5, 6])

dot = np.dot(row, col)
print("\nDot Product:", dot)

# Simple ML Example
# z = w.x + b

w = np.array([0.5, 0.3])
x = np.array([4, 10])
b = 2

z = np.dot(w, x) + b
print("\nLinear Model Output:", z)

#Confusion Matrix Example
TP = 50
TN = 35
FP = 5
FN = 10

accuracy = (TP + TN) / (TP + TN + FP + FN)
print("\nAccuracy:", accuracy)