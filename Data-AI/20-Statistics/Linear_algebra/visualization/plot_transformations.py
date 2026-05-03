import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(vectors, colors, labels, title):
    for v, c, l in zip(vectors, colors, labels):
        plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=c, label=l)

    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()


v = np.array([2,3])

# Scaling
scaled = 2 * v

# Rotation
theta = np.pi/2
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
rotated = R @ v

# Reflection
A = np.array([[-1,0],[0,1]])
reflected = A @ v

plot_vectors(
    [v, scaled, rotated, reflected],
    ['blue', 'green', 'red', 'purple'],
    ['Original', 'Scaled', 'Rotated', 'Reflected'],
    "Transformations Visualization"
)