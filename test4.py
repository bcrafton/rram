
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram5 import rram

r = rram(shape=(2, 2), deltaGap0=0.05, model_switch=0)

T = 205e-9
dt = 1e-12
pulse_width = 100e-9
steps = int(T / dt) + 1
Ts = np.linspace(0., T, steps)

Vs = ((signal.square(2 * np.pi * (1. / (2 * pulse_width)) * Ts, duty=0.5) + 1.) / 2.) * -1.3
Is = []

for v in Vs:
    i = -r.step(v, dt)
    Is.append(i)
  
plt.subplot(3, 1, 1)
plt.plot(Ts, Vs)
    
plt.subplot(3, 1, 2)
plt.plot(Ts, Is)

# plt.subplot(3, 1, 3)
# plt.plot(Vs, Is)

plt.show()

# this matches figure 5 perfectly.
# Figure 5. Typical Pulse Operation without Variations (SET and RESET)
