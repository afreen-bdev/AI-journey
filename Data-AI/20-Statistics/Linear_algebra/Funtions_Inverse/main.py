import numpy as np
from funtions.inverse_functions import inverse_linear
from matrices.matrix_inverse import inverse_2x2

def main():
    # Function inverse
    y = 7
    x = inverse_linear(2, 3, y)
    print("Inverse function result:", x)

    # Matrix inverse
    A = np.array([[4, 7], [2, 6]])
    print("Matrix inverse:\n", inverse_2x2(A))

if __name__ == "__main__":
    main()