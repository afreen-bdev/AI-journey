import numpy as np

def inverse_2x2(A):
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0]

    if det == 0:
        raise ValueError("Matrix not invertible")

    inv = (1/det) * np.array([
        [A[1][1], -A[0][1]],
        [-A[1][0], A[0][0]]
    ])

    return inv


def inverse_numpy(A):
    return np.linalg.inv(A)