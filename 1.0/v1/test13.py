
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram6 import rram

t_ramp = 100e-3
vdd = 1.3

############################
'''
r = rram(shape=(2, 2), gap_ini=19e-10, deltaGap0=1e-4, model_switch=0)

dt = 1e-7
Vs = np.concatenate((np.linspace(0., vdd, t_ramp/dt), np.linspace(vdd, vdd, 1e-6/dt), np.linspace(vdd, 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []

for v in Vs:
    i = r.step(v, dt)
    Is.append(i)
'''
############################

r = rram(shape=(2, 2), gap_ini=2e-10, deltaGap0=1e-4, model_switch=0)

dt = 1e-7
Vs = np.concatenate((np.linspace(0., -vdd, t_ramp/dt), np.linspace(-vdd, -vdd, 1e-6/dt), np.linspace(-vdd, 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []

for v in Vs:
    i = r.step(v, dt)
    Is.append(i)
  
Is = np.array(Is) * -1.

############################
  
Ts = np.linspace(0., steps*dt, steps)
Rs = np.absolute(Vs) / np.absolute(Is) # (np.absolute(Vs) + 1e-12) / (np.absolute(Is) + 1e-12)
idx = np.where(np.isnan(Rs)==False)
print (np.max(Rs[idx]), np.min(Rs[idx]), np.max(Rs[idx]) / np.min(Rs[idx]))

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

