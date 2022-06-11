import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

n = 50
u0 = 1
v = 1
H = 1
deltaH = H/n

'''colour = np.zeros((n+1))
for i in range(len(colour)):
    colour[i] = tuple((0.5, 0.5, i/n+1))
    print(colour)

print(colour)'''

color = [str(item/(n+1)) for item in range(n+1)]
print(color)

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
    dudt = (A@u)/(deltaH**2)
    return dudt

z = odeint(model, y0 = u, t = t)
z = np.array(z)

# plot results
plt.plot(t,z,color='red',linewidth=2,label='u')
plt.xlabel('time')
plt.ylabel('u')
plt.show()