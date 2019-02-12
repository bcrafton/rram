
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram7 import rram

t_ramp = 1e-6
vdd = 2.
dt = 1e-10

############################

r = rram(shape=(2, 2), gap_min=2e-10, gap_max=19e-10, gap_ini=19e-10, I0=1e-6, g0=0.25e-9, deltaGap0=1e-4, model_switch=0)

Vs = np.concatenate((np.linspace(0., vdd, t_ramp/dt), np.linspace(vdd, vdd, 1e-6/dt), np.linspace(vdd, 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []
Rs = []

for v in Vs:
    Rs.append(r.R())
    i = r.step(v, dt)
    Is.append(i)

Vs1 = np.copy(Vs)
Is1 = np.copy(Is)
Rs1 = np.copy(Rs)

############################

r = rram(shape=(2, 2), gap_min=2e-10, gap_max=19e-10, gap_ini=2e-10, I0=1e-6, g0=0.25e-9, deltaGap0=1e-4, model_switch=0)

Vs = np.concatenate((np.linspace(0., -vdd, t_ramp/dt), np.linspace(-vdd, -vdd, 1e-6/dt), np.linspace(-vdd, 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []
Rs = []

for v in Vs:
    Rs.append(r.R())
    i = r.step(v, dt)
    Is.append(i)
  
Is = np.array(Is) * -1.

Vs2 = np.copy(Vs)
Is2 = np.copy(Is)
Rs2 = np.copy(Rs)

############################
  
Ts = np.linspace(0., 2*steps*dt, 2*steps)
Vs = np.concatenate((Vs1, Vs2))
Is = np.concatenate((Is1, Is2))
Rs = np.concatenate((Rs1, Rs2))

############################

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 10.
f, ax = plt.subplots(2, 1)
f.set_size_inches(3.5, 3.5)

ax[0].semilogy(Vs, Is)
ax[1].semilogy(Ts, Rs)

plt.show()
############################

