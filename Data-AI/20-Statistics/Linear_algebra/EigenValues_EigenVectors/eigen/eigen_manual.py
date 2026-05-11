import numpy as np

def characteristic_equation(A):
    trace = A[0][0] + A[1][1]
    determinant = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

    print(f"λ² - ({trace})λ + ({determinant}) = 0")


def verify_eigen(A, eigenvalue, eigenvector):
    left = A @ eigenvector
    right = eigenvalue * eigenvector

    return np.allclose(left, right)