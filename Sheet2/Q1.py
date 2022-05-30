import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns du1/dt
def model(z,t):
    u1 = z[0]
    u2 = z[1]
    u3 = z[2]
    du1dt = -u1
    du2dt = u1-u2
    du3dt = u2-u3
    dzdt = [du1dt, du2dt, du3dt]
    return dzdt



# initial condition
z0 = [1, 2, 3]

# time points
t = np.linspace(0,5)

# solve ODE
z = odeint(model,z0,t)
z = np.array(z)
u1 = z[:,0]
u2 = z[:,1]
u3 = z[:,2]


#real solution
#y = 2 - np.exp(-t)

# plot results
plt.plot(t,u1,'r-',linewidth=2,label='u1')
plt.plot(t,u2,'b-',linewidth=2,label='u2')
plt.plot(t,u3,'g-',linewidth=2,label='u3')
#plt.plot(t,y,'b--',linewidth=2,label='Real')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()