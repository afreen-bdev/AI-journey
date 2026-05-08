from sklearn.preprocessing import StandardScaler
import numpy as np

def sklearn_scaling():
    data = np.array([[1], [2], [3], [4]])

    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)

    original = scaler.inverse_transform(scaled)

    return scaled, original