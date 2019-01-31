
import numpy as np
import os
import copy
import threading
import argparse

################################################

def get_perms(param):
    params = [param]
    
    for key in param.keys():
        val = param[key]
        if type(val) == list:
            new_params = []
            for ii in range(len(val)):
                for jj in range(len(params)):
                    new_param = copy.copy(params[jj])
                    new_param[key] = val[ii]
                    new_params.append(new_param)
                    
            params = new_params
            
    return params

################################################

gap_min = np.linspace(-11., -10., 10)
gap_min = np.power(10., gap_min)
gap_min = gap_min.tolist()
gap_min = [1e-11, 2e-11, 3e-11, 4e-11, 5e-11, 6e-11, 7e-11, 8e-11, 9e-11, 10e-11]

gap_max = np.linspace(-10., -8., 10)
gap_max = np.power(10., gap_max)
gap_max = gap_max.tolist()
gap_max = [1e-10, 2e-10, 3e-10, 4e-10, 5e-10, 6e-10, 7e-10, 8e-10, 9e-10, 10e-10]

I0 = np.linspace(-8., -3., 10)
I0 = np.power(10., I0)
I0 = I0.tolist()

g0 = np.linspace(-11., -7., 10)
g0 = np.power(10., g0)
g0 = g0.tolist()

rram = {'benchmark':'test2.py', 'gap_min':gap_min, 'gap_max':gap_max, 'I0':I0, 'g0':g0}

###############################################

params = [rram]

################################################

def get_runs():
    runs = []

    for param in params:
        perms = get_perms(param)
        runs.extend(perms)

    return runs

################################################

        
