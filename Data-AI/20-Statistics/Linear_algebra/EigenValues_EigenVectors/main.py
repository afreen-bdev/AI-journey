import numpy as np

from eigen.eigen_basic import compute_eigen
from eigen.eigen_manual import verify_eigen

A = np.array([
    [4,1],
    [2,3]
])

eigenvalues, eigenvectors = compute_eigen(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

v = eigenvectors[:,0]
lam = eigenvalues[0]

print("\nVerification:")
print(verify_eigen(A, lam, v))