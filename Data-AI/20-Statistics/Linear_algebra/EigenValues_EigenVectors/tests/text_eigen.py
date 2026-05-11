import numpy as np
from eigen.eigen_manual import verify_eigen

def test_eigen():
    A = np.array([[4,1],[2,3]])

    eigenvalue = 5
    eigenvector = np.array([1,1])

    assert verify_eigen(A, eigenvalue, eigenvector)