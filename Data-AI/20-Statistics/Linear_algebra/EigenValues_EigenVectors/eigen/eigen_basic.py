import numpy as np

def compute_eigen(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)

    return eigenvalues, eigenvectors