
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram4 import rram

r = rram(shape=(2, 2))

T = 205e-9
dt = 1e-12
pulse_width = 10e-12
steps = int(T / dt) + 1
Ts = np.linspace(0., T, steps)

Vs = (signal.square(2 * np.pi * (1. / pulse_width) * Ts) - 1.) * (1.3 / 2.)
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
