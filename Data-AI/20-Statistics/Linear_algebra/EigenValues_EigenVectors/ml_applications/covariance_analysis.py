import numpy as np

def covariance_matrix(data):
    return np.cov(data.T)