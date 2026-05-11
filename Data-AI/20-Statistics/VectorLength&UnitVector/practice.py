import numpy as np
from vector_operations import vector_length, unit_vector
from cosine_similarity import cosine_similarity

# Problem 1
v1 = np.array([3, 4])
print("P1 Length:", vector_length(v1)) 

# Problem 2
v2 = np.array([1, 2, 2])
print("P2 Unit Vector:", unit_vector(v2))

# Problem 3
v3 = np.array([0, 0, 0])
try:
    print("P3 Unit Vector:", unit_vector(v3))
except ValueError as e:
    print("P3 Error:", e)

# Problem 4
a = np.array([1, 0])
b = np.array([0, 1])
print("P4 Cosine Similarity:", cosine_similarity(a, b))  # Expected: 0

# Problem 5
c = np.array([1, 2])
d = np.array([2, 4])
print("P5 Cosine Similarity:", cosine_similarity(c, d))  # Expected: 1