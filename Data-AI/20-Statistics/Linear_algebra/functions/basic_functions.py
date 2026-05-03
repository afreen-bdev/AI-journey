import numpy as np

# f(x) = 2x + 3
def scalar_function(x):
    return 2*x + 3

print("Scalar Function:")
print("f(5) =", scalar_function(5))

# Vector function: f(x,y,z) = (x+y, 2z)
def vector_function(v):
    x, y, z = v
    return np.array([x + y, 2*z])

v = np.array([1,2,3])
print("\nVector Function:")
print("Input:", v)
print("Output:", vector_function(v))