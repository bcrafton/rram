
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram import rram

####################################

# X1 mid1 mid2 RRAM_v_2_0_Beta x0=0    w0=5e-9   Ei=0.82 Eh=1.12 deltaGap=4e-5   **x0=0, w0=5nm are initial conditions for RESET
# X1 mid1 mid2 RRAM_v_2_0_Beta x0=3e-9 w0=0.5e-9 

####################################

dt = 1e-7
Vs = np.concatenate((
np.linspace(0., 2., int(10e-6/dt)), 
np.linspace(2., 2., int(80e-6/dt)), 
np.linspace(2., 0., int(10e-6/dt))
))

####################################

# r = rram(x0=3e-9, w0=0.5e-9)
r = rram(x0=0., w0=5e-9)

Vs1 = Vs * -1.
steps = np.shape(Vs1)[0] 
Is1 = []

for v in Vs1:
    i = r.step(v, dt)
    Is1.append(i)
  
Is1 = np.array(Is1) * -1.

####################################

r = rram(x0=3e-9, w0=0.5e-9)
# r = rram(x0=0., w0=5e-9)

Vs2 = Vs
Is2 = []

for v in Vs2:
    i = r.step(v, dt)
    Is2.append(i)

####################################

Ts = np.linspace(0., 2*steps*dt, 2*steps)
Vs = np.concatenate((Vs1, Vs2))
Is = np.concatenate((Is1, Is2))
# Rs = np.where(np.absolute(Is) == 0, np.zeros_like(Is), Vs / Is)

####################################

plt.subplot(4, 1, 1)
plt.plot(Ts, Vs)
    
plt.subplot(4, 1, 2)
plt.plot(Ts, Is)

plt.subplot(4, 1, 3)
plt.semilogy(Vs, Is)

# plt.subplot(4, 1, 4)
# plt.plot(Ts, Rs)

plt.show()

####################################


