import numpy as np

# 90 degree rotation
theta = np.pi / 2

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

v = np.array([1,0])

rotated = R @ v

print("Rotation:")
print("Original:", v)
print("Rotated:", rotated)