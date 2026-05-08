import numpy as np

def standardize(x):
    mean = np.mean(x)
    std = np.std(x)
    z = (x - mean) / std
    return z, mean, std


def inverse_standardize(z, mean, std):
    return z * std + mean


def minmax(x):
    min_val = np.min(x)
    max_val = np.max(x)
    z = (x - min_val) / (max_val - min_val)
    return z, min_val, max_val


def inverse_minmax(z, min_val, max_val):
    return z * (max_val - min_val) + min_val