import numpy as np

A = np.array([
    [-1, 0],
    [0, 1]
])

u = np.array([1,2])
v = np.array([3,4])
c = 2

# Additivity
left1 = A @ (u + v)
right1 = A @ u + A @ v

# Homogeneity
left2 = A @ (c * u)
right2 = c * (A @ u)

print("Additivity Check:", np.allclose(left1, right1))
print("Homogeneity Check:", np.allclose(left2, right2))