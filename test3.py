
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram4 import rram

r = rram(shape=(2, 2))

dt = 1e-7
Vs = np.concatenate((np.linspace(0., -2., 4e-3/dt), np.linspace(-2., -2., 1e-6/dt), np.linspace(-2., 0., 4e-3/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []

for v in Vs:
    i = r.step(v, dt)
    Is.append(i)
  
plt.subplot(3, 1, 1)
plt.plot(Ts, Vs)
    
plt.subplot(3, 1, 2)
plt.plot(Ts, Is)

plt.subplot(3, 1, 3)
plt.plot(Vs, Is)

plt.show()
