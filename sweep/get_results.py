
import numpy as np
import os
import copy
import threading
import argparse
from results import get_runs

##############################################

runs = get_runs()
_results = []

##############################################

num_runs = len(runs)
for ii in range(num_runs):
    param = runs[ii]

    # figure out the name of the param
    name = './results/%0.12f_%0.12f_%0.12f.npy' % (param['I0'], param['V0'], param['g0'])

    # load the results
    try:
        results = np.load(name)
        _max = np.max(results)
        _min = np.min(results)
        _ratio = np.max(results) / np.min(results)
        # print (_max, _min, _ratio)
        _results.append([_max, _min, _ratio])

    except:
        pass
            
##############################################

_results = np.array(_results)
idx1 = np.where( (_results[:, 0] > 1e7) * (_results[:, 0] < 1e9) )
idx2 = np.where( (_results[:, 1] > 1e5) * (_results[:, 1] < 1e7) )
idx3 = np.where( (_results[:, 2] > 1e1) * (_results[:, 2] < 1e3) )

# print (idx1)
# print (idx2)
# print (idx3)

idx = np.intersect1d(idx1, idx2)
idx = np.intersect1d(idx, idx3)

print (idx)
print (_results[idx, :])

##############################################

_results = np.array(_results)
idx1 = np.where( (_results[:, 0] > 5e7) * (_results[:, 0] < 5e8) )
idx2 = np.where( (_results[:, 1] > 5e5) * (_results[:, 1] < 5e6) )
idx3 = np.where( (_results[:, 2] > 75.) * (_results[:, 2] < 150.) )

# print (idx1)
# print (idx2)
# print (idx3)

idx = np.intersect1d(idx1, idx2)
idx = np.intersect1d(idx, idx3)

print (idx)
print (_results[idx, :])




