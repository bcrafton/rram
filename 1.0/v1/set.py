
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from rram5 import rram
from pulse import pulse

r = rram(shape=(2, 2), gap_ini=17e-10, deltaGap0=1e-4, model_switch=0)

dt = 1e-8
# Vs = np.concatenate((np.linspace(0., 2., int(4e-3/dt)), np.linspace(2., 2., int(1e-6/dt)), np.linspace(2., 0., int(4e-3/dt))))
Vs = pulse(100, 5, 5, 0.01, 1.4)
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []

for v in Vs:
    i = r.step(v, dt)
    Is.append(i)
  
plt.subplot(2, 1, 1)
plt.plot(Ts * 1e9, Vs)
plt.ylim(0, 2)

plt.subplot(2, 1, 2)
Vs = np.array(Vs)
Is = np.array(Is)
plt.plot(Ts * 1e9, Is * 1e6)

plt.gcf().tight_layout()
plt.savefig('set.png', dpi=300)
# plt.show()

