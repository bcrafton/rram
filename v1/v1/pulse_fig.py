
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram5 import rram

r = rram(shape=(2, 2), gap_ini=2e-10, deltaGap0=0.05, model_switch=0)

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
  
############################################################

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 10.
f, ax = plt.subplots(2, 1)
f.set_size_inches(3.5, 4.)

ax[0].plot(Ts, Vs)
ax[1].plot(Ts, Is)

plt.savefig('memristor_pulse.png', dpi=1000, bbox_inches='tight')

############################################################
