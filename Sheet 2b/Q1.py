import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

n = 50
u0 = 1

u = np.linspace(0,5, num = n+1)

# Get A
A = np.zeros((n+1, n+1))
A[0, 0] = u0
A[n, n] = u0
for i in range(1, n):
    A[i, i-1] = 1
    A[i, i] = -2
    A[i, i+1] = 1

def model(u):
    dudt = A*u
    return dudt

print(A@u)
