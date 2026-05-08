import numpy as np

def log_transform(x):
    return np.log(x)

def inverse_log(y):
    return np.exp(y)