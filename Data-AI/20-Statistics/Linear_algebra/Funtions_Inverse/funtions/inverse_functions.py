def inverse_linear(a, b, y):
    """
    f(x) = ax + b
    f⁻¹(y) = (y - b)/a
    """
    if a == 0:
        raise ValueError("Not invertible")
    return (y - b) / a


def verify_inverse(f, f_inv, x):
    return f_inv(f(x)) == x