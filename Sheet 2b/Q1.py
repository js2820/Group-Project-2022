import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

n = 50
u0 = 1
t = np.linspace(0,10)


u = np.zeros(n+1)
u[0] = u0
u[n] = u0

# Get A
A = np.zeros((n+1, n+1))
A[0, 0] = 1
A[n, n] = 1
for i in range(1, n):
    A[i, i-1] = 1
    A[i, i] = -2
    A[i, i+1] = 1

def model(u, t):
    dudt = A@u
    return dudt

z = odeint(model, y0 = u, t = t)

# plot results
plt.plot(t,z,'r-',linewidth=2,label='u')
plt.xlabel('time')
plt.ylabel('Difference')
plt.show()