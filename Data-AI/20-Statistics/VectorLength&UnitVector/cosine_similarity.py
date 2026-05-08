import numpy as np

def cosine_similarity(a, b):
    """
    cos(theta) = (A.B) / (||A|| * ||B||)
    """
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    return dot / (norm_a * norm_b)


# Test
if __name__ == "__main__":
    a = np.array([1, 2])
    b = np.array([2, 3])

    print("Cosine Similarity:", cosine_similarity(a, b))