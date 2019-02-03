
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram import rram

r = rram()

####################################

r = rram()

dt = 1e-7
Vs1 = np.concatenate((np.linspace(0., -2., 4e-3/dt), np.linspace(-2., -2., 1e-6/dt), np.linspace(-2., 0., 4e-3/dt)))
steps = np.shape(Vs1)[0] 
Is1 = []

for v in Vs1:
    i = r.step(v, dt)
    Is1.append(i)
  
Is1 = np.array(Is1) * -1.

####################################

r = rram()

dt = 1e-7
Vs2 = np.concatenate((np.linspace(0., 2., 4e-3/dt), np.linspace(2., 2., 1e-6/dt), np.linspace(2., 0., 4e-3/dt)))
steps = np.shape(Vs2)[0] 
Is2 = []

for v in Vs2:
    i = r.step(v, dt)
    Is2.append(i)

####################################

Ts = np.linspace(0., 2*steps*dt, 2*steps)
Vs = np.concatenate((Vs1, Vs2))
Is = np.concatenate((Is1, Is2))

print (np.shape(Vs))
print (np.shape(Is))

print (np.min(Vs))
print (np.max(Vs))

print (np.min(Is))
print (np.max(Is))

####################################

plt.subplot(3, 1, 1)
plt.plot(Ts, Vs)
    
plt.subplot(3, 1, 2)
plt.plot(Ts, Is)

plt.subplot(3, 1, 3)
plt.semilogy(Vs, Is)

plt.show()
