
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

I0 = np.linspace(-8., -3., 10)
I0 = np.power(10., I0)
I0 = I0.tolist()

V0 = np.linspace(0.1, 1.0, 10)
V0 = V0.tolist()

g0 = np.linspace(-11., -8., 10)
g0 = np.power(10., g0)
g0 = g0.tolist()

rram = {'benchmark':'test.py', 'I0':I0, 'V0':V0, 'g0':g0}

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

        
