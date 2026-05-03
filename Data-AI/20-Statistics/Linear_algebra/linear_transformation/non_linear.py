import numpy as np

def T(x):
    b = np.array([1,1])
    return x + b

u = np.array([2,3])
v = np.array([4,-1])
c = 2

print("Non-linear Transformation:")

print("\nAdditivity:")
print("T(u+v):", T(u+v))
print("T(u)+T(v):", T(u)+T(v))

print("\nHomogeneity:")
print("T(cu):", T(c*u))
print("cT(u):", c*T(u))