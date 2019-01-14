
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram5 import rram

r = rram(shape=(2, 2), deltaGap0=1e-4, model_switch=0)

dt = 1e-8
Vs = np.concatenate((np.linspace(2., -2., 1e-4/dt), np.linspace(-2., -2., 1e-6/dt), np.linspace(-2., 2., 1e-4/dt)))
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
