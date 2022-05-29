import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(u,t):
    dydt = np.exp(-t)
    return dydt

# initial condition
u0 = 1

# time points
t = np.linspace(0,5)

# solve ODE
u = odeint(model,u0,t)

#real solution
y = 2 - np.exp(-t)

# plot results
plt.plot(t,u,'r-',linewidth=2,label='Computer')
plt.plot(t,y,'b--',linewidth=2,label='Real')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()