import numpy as np
import matplotlib.pyplot as plt

n = 1000000

#Generate grid between 0 and 2pi
t = np.linspace(0, 2*np.pi, num=n)

h = (2/n)*np.pi

#Sin over t
f = np.sin(t)

#First diff of f
f1 = np.diff(f)/h
t1_diff = t[:-1:] 

#Second diff of f
f2 = np.diff(f1)/h
t2_diff = t1_diff[:-1:] 

plt.plot(t,f,'b-',linewidth=2,label='f')
plt.plot(t1_diff,f1,'g-',linewidth=2,label='f1')
plt.plot(t2_diff,f2,'r-',linewidth=2,label='f2')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()