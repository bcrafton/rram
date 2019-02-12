
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import argparse
from rram_dr import rram
from scipy.interpolate import interp1d

t_ramp = 1e-6
vdd = 1.
dt = 1e-10

############################
parser = argparse.ArgumentParser()
parser.add_argument('--gap_min', type=float, default=2e-10)
parser.add_argument('--gap_max', type=float, default=19e-10)
parser.add_argument('--I0', type=float, default=1e-6)
parser.add_argument('--g0', type=float, default=0.375e-9)
args = parser.parse_args()

print (args)

gap_min=args.gap_min
gap_max=args.gap_max
I0=args.I0
g0=args.g0
deltaGap0=1e-4
model_switch=0
############################
r = rram(shape=(1, 1), gap_min=gap_min, gap_max=gap_max, gap_ini=gap_max/2., I0=I0, g0=g0, deltaGap0=deltaGap0, model_switch=model_switch)

Vs = np.concatenate((np.linspace(0., -vdd, t_ramp/dt), np.linspace(-vdd, -vdd, 1e-6/dt), np.linspace(-vdd, 0., t_ramp/dt)))
steps = np.shape(Vs)[0] 
Ts = np.linspace(0., steps*dt, steps)
Is = []
Rs = []

for v in Vs:
    Rs.append(r.R()[0][0])
    i = r.step(np.reshape(v, (1, 1)), dt)
    Is.append(i[0][0])
  
Is = np.array(Is) * -1.

Vs2 = np.copy(Vs)
Is2 = np.copy(Is)
Rs2 = np.copy(Rs)
############################
Ts = np.linspace(0., steps*dt, steps)
Vs = Vs2
Is = Is2
Rs = Rs2
############################
results = {'V': Vs, 'dR':Is}
np.save('drdv', results)
drdv = np.load('drdv.npy').item()
fit = interp1d(drdv['V'], drdv['dR'])
dR = fit(Vs)

# print (fit(-0.8))

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.size'] = 10.
f, ax = plt.subplots(1, 1)
f.set_size_inches(3.5, 3.5)

# ax.plot(Vs, Is)
ax.plot(Vs, dR)
plt.show()
############################






