
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram5 import rram

t_ramp = 10e-3

############################
r = rram(shape=(2, 2), gap_ini=19e-10, deltaGap0=1e-4, model_switch=0)

dt = 1e-7
Vs = np.concatenate((np.linspace(0., 2., t_ramp/dt), np.linspace(2., 2., 1e-6/dt), np.linspace(2., 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []

for v in Vs:
    i = r.step(v, dt)
    Is.append(i)

Vs1 = np.copy(Vs)
Is1 = np.copy(Is)

############################

r = rram(shape=(2, 2), gap_ini=2e-10, deltaGap0=1e-4, model_switch=0)

dt = 1e-7
Vs = np.concatenate((np.linspace(0., -2., t_ramp/dt), np.linspace(-2., -2., 1e-6/dt), np.linspace(-2., 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []

for v in Vs:
    i = r.step(v, dt)
    Is.append(i)
  
Is = np.array(Is) * -1.

Vs2 = np.copy(Vs)
Is2 = np.copy(Is)

############################
  
Ts = np.linspace(0., 2*steps*dt, 2*steps)
Vs = np.concatenate((Vs1, Vs2))
Is = np.concatenate((Is1, Is2)) # / 1e3
  
############################

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 10.
f, ax = plt.subplots(2, 1)
f.set_size_inches(3.5, 3.5)

ax[0].semilogy(Vs, Is)
ax[1].semilogy(Ts, (np.absolute(Vs) + 1e-12) / (np.absolute(Is) + 1e-12))

plt.show()
# plt.savefig('memristor_dc.png', dpi=1000, bbox_inches='tight')
############################

