import numpy as np

def diagonalize(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)

    D = np.diag(eigenvalues)

    P = eigenvectors

    P_inv = np.linalg.inv(P)

    reconstructed = P @ D @ P_inv

    return D, reconstructed