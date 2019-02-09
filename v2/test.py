
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram import rram

####################################

# X1 mid1 mid2 RRAM_v_2_0_Beta x0=0    w0=5e-9   Ei=0.82 Eh=1.12 deltaGap=4e-5   **x0=0, w0=5nm are initial conditions for RESET
# X1 mid1 mid2 RRAM_v_2_0_Beta x0=3e-9 w0=0.5e-9 

####################################

r = rram(x0=3e-10, w0=5e-9)

dt = 1e-12
Vs1 = np.concatenate((np.linspace(0., 2., 1e-9/dt), np.linspace(2., 2., 8e-9/dt), np.linspace(2., 0., 1e-9/dt)))
Vs1 = Vs1 * -1.
steps = np.shape(Vs1)[0] 
Is1 = []

for v in Vs1:
    i = r.step(v, dt)
    Is1.append(i)
  
Is1 = np.array(Is1) * -1.

####################################

r = rram(x0=3e-9, w0=0.5e-9)

dt = 1e-12
Vs2 = np.concatenate((np.linspace(0., 2., 1e-9/dt), np.linspace(2., 2., 8e-9/dt), np.linspace(2., 0., 1e-9/dt)))
steps = np.shape(Vs2)[0] 
Is2 = []

for v in Vs2:
    i = r.step(v, dt)
    Is2.append(i)

####################################

Ts = np.linspace(0., 2*steps*dt, 2*steps)
Vs = np.concatenate((Vs1, Vs2))
Is = np.concatenate((Is1, Is2))

'''
Ts = np.linspace(0., steps*dt, steps)
Vs = Vs1
Is = Is1
'''
####################################

plt.subplot(3, 1, 1)
plt.plot(Ts, Vs)
    
plt.subplot(3, 1, 2)
plt.plot(Ts, Is)

plt.subplot(3, 1, 3)
plt.semilogy(Vs, Is)

plt.show()
