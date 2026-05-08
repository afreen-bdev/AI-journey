import numpy as np

def vector_length(v):
    """
    Compute Euclidean norm (L2 norm)
    ||v|| = sqrt(x1^2 + x2^2 + ... + xn^2)
    """
    return np.linalg.norm(v)


def unit_vector(v):
    """
    Convert vector to unit vector
    u = v / ||v||
    """
    norm = np.linalg.norm(v)
    if norm == 0:
        raise ValueError("Zero vector has no direction")
    return v / norm


# Test
if __name__ == "__main__":
    v = np.array([2, 3])
    print("Vector:", v)
    print("Length:", vector_length(v))
    print("Unit Vector:", unit_vector(v))