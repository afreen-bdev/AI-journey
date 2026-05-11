import numpy as np
import matplotlib.pyplot as plt

def plot_vectors():
    A = np.array([[4,1],
                  [2,3]])

    eigenvalues, eigenvectors = np.linalg.eig(A)

    origin = [0,0]

    plt.quiver(*origin,
               eigenvectors[0,:],
               eigenvectors[1,:],
               angles='xy',
               scale_units='xy',
               scale=1)

    plt.xlim(-2,2)
    plt.ylim(-2,2)

    plt.grid()
    plt.title("Eigenvectors")
    plt.show()