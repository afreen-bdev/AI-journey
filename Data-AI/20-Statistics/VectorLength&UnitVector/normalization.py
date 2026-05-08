import numpy as np

def normalize_dataset(X):
    """
    Normalize each row vector to unit length
    """
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    return X / norms


# Test
if __name__ == "__main__":
    X = np.array([
        [50, 100000],
        [30, 50000]
    ])

    print("Original:\n", X)
    print("Normalized:\n", normalize_dataset(X))