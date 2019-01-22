
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import argparse
from rram import rram

##############################################

parser = argparse.ArgumentParser()
parser.add_argument('--I0', type=float, default=1e-6)
parser.add_argument('--V0', type=float, default=0.25)
parser.add_argument('--g0', type=float, default=0.25e-9)
args = parser.parse_args()

name = './results/%0.12f_%0.12f_%0.12f.npy' % (args.I0, args.V0, args.g0)

##############################################

t_ramp = 10e-3

############################

r = rram(shape=(2, 2), gap_ini=19e-10, deltaGap0=1e-4, model_switch=0, I0=args.I0, V0=args.V0, g0=args.g0)

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

r = rram(shape=(2, 2), gap_ini=2e-10, deltaGap0=1e-4, model_switch=0, I0=args.I0, V0=args.V0, g0=args.g0)

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
Rs = np.absolute(Vs) / np.absolute(Is) # (np.absolute(Vs) + 1e-12) / (np.absolute(Is) + 1e-12)
idx = np.where(np.isnan(Rs)==False)
Rs = Rs[idx]
np.save(name, Rs)

############################

