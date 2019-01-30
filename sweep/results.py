
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
'''
gap_min = np.linspace(-10., -8., 10)
gap_min = np.power(10., gap_min)
gap_min = gap_min.tolist()

gap_max = np.linspace(-9., -7., 10)
gap_max = np.power(10., gap_max)
gap_max = gap_max.tolist()
'''

# 1.00000000e-10 2.15443469e-08 4.64158883e-07 4.64158883e-09

gap_min = [1e-10]

gap_max = [25e-10]

I0 = np.linspace(-8., -3., 10)
I0 = np.power(10., I0)
I0 = I0.tolist()

g0 = np.linspace(-11., -7., 10)
g0 = np.power(10., g0)
g0 = g0.tolist()

gap_min = [1.00000000e-10]
gap_max = [ 2.15443469e-08] 
I0 = [4.64158883e-07]
g0 = [4.64158883e-09]

rram = {'benchmark':'test.py', 'gap_min':gap_min, 'gap_max':gap_max, 'I0':I0, 'g0':g0}

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

        
