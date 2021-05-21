
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import argparse
from rram import rram

t_ramp = 1e-4
vdd = 2.0
dt = 1e-9
N = 2

############################

# average switching fitting parameters g0, V0, I0, beta, gamma0

############################

r = rram()

Vs1 = np.concatenate((np.linspace(0., -vdd, int(t_ramp/dt)), np.linspace(-vdd, -vdd, int(1e-6/dt)), np.linspace(-vdd, 0., int(t_ramp/dt))))
Vs2 = np.concatenate((np.linspace(0., vdd, int(t_ramp/dt)), np.linspace(vdd, vdd, int(1e-6/dt)), np.linspace(vdd, 0., int(t_ramp/dt))))
Vs = np.concatenate((Vs1, Vs2))
# this is a bit of nonsense here.
Vs = np.reshape(Vs, (1, -1))
Vs = np.repeat(Vs, N, axis=0)
Vs = np.reshape(Vs, (-1))

# x = np.array([1, 2, 3, 4])
# array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])

steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []
Rs = []
dRs = []

for v in Vs:
    pre_r = r.R()
    Rs.append(pre_r)
    i = r.step(v, dt)
    post_r = r.R()
    Is.append(i)
    dRs.append(post_r - pre_r)

############################

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 10.
f, ax = plt.subplots(4, 1)

ax[0].semilogy(Vs, np.absolute(Is))
ax[1].plot(Ts, Vs)
ax[2].semilogy(Ts, np.absolute(Is))
ax[3].semilogy(Ts, Rs)

print (np.max(Rs) / np.min(Rs))

plt.show()
############################

