import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

A = np.array([1, 1])
B = np.array([2, 2])
C = np.array([1, -1])

print("A vs B:", cosine_similarity(A, B))
print("A vs C:", cosine_similarity(A, C))