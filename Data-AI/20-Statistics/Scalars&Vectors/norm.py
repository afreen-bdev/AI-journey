import numpy as np

x = np.array([3, 4])

norm = np.linalg.norm(x)

print("Vector:", x)
print("Magnitude (L2 norm):", norm)

# Unit vector
unit_vector = x / norm
print("Unit vector:", unit_vector)