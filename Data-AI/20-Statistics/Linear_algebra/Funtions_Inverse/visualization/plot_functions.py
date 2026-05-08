import numpy as np
import matplotlib.pyplot as plt

def plot_inverse():
    x = np.linspace(-10, 10, 100)
    y = 2*x + 3
    y_inv = (x - 3) / 2

    plt.plot(x, y, label="f(x)")
    plt.plot(x, y_inv, label="f⁻¹(x)")
    plt.legend()
    plt.grid()
    plt.show()