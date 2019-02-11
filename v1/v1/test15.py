
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram7 import rram

############################

def square(T, dt, pulse_width):
    steps = int(T / dt) + 1
    Ts = np.linspace(0., steps*dt, steps)
    ret = (signal.square(2 * np.pi * (1. / (2 * pulse_width)) * Ts, duty=0.5) + 1.) / 2.
    return ret

############################

r = rram(shape=(2, 2), gap_ini=2e-10, deltaGap0=1e-4, model_switch=0)

dt = 1e-11
pulse_width = 1e-8
T = 1e-5
steps = int(T / dt) + 1
vdd = 1.5

Ts = np.linspace(0., steps*dt, steps)
Vs = square(T, dt, pulse_width) * -vdd
Is = []
Rs = []

for v in Vs:
    Rs.append(r.R())
    i = r.step(v, dt)
    Is.append(i)
  
Is = np.array(Is) * -1.

############################
  
Ts = np.linspace(0., steps*dt, steps)
# Rs = np.absolute(Vs) / np.absolute(Is) # (np.absolute(Vs) + 1e-12) / (np.absolute(Is) + 1e-12)
# idx = np.where(np.isnan(Rs)==False)
# print (np.max(Rs[idx]), np.min(Rs[idx]), np.max(Rs[idx]) / np.min(Rs[idx]))
print (np.max(Rs), np.min(Rs))
print (r.gap)

############################

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 10.
f, ax = plt.subplots(3, 1)
# f.set_size_inches(3.5, 3.5)

ax[0].plot(Ts, Vs)
ax[1].plot(Ts, Is)
ax[2].plot(Ts, Rs / np.min(Rs))

plt.show()
############################

