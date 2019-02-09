
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import argparse
from rram import rram

t_ramp = 1e-6
vdd = 2.
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

r = rram(shape=(2, 2), gap_min=gap_min, gap_max=gap_max, gap_ini=gap_max, I0=I0, g0=g0, deltaGap0=deltaGap0, model_switch=model_switch)

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

r = rram(shape=(2, 2), gap_min=gap_min, gap_max=gap_max, gap_ini=gap_min, I0=I0, g0=g0, deltaGap0=deltaGap0, model_switch=model_switch)

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

ratio = np.max(Rs) / np.min(Rs)

flag = True
flag = flag and (np.min(Rs) > 5e5) and (np.min(Rs) < 5e6) 
flag = flag and (np.max(Rs) > 5e7) and (np.max(Rs) < 5e8)
flag = flag and (ratio > 90.)      and (ratio < 150.)

print (np.min(Rs) / 1e6, np.max(Rs) / 1e6, ratio)

flag = True

if flag:
    plt.rcParams['font.sans-serif'] = "Arial"
    plt.rcParams['font.family'] = "sans-serif"
    plt.rcParams['font.size'] = 10.
    f, ax = plt.subplots(2, 1)
    f.set_size_inches(3.5, 3.5)

    ax[0].semilogy(Vs, Is)
    ax[1].semilogy(Ts, Rs)

    name = '%0.12f_%0.12f_%0.12f_%0.12f.png' % (args.gap_min, args.gap_max, args.I0, args.g0)
    plt.show()
    
############################

