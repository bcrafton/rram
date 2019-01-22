
import numpy as np
import os
import copy
import threading
import argparse

from results import get_runs

##############################################

parser = argparse.ArgumentParser()
parser.add_argument('--print', type=int, default=0)
cmd_args = parser.parse_args()

##############################################

def run_command(param):
    
    name = '%s_%0.12f_%0.12f_%0.12f' % (param['benchmark'], param['I0'], param['V0'], param['g0'])
    
    cmd = "python %s --I0 %0.12f --V0 %0.12f --g0 %0.12f" % (param['benchmark'], param['I0'], param['V0'], param['g0'])

    if cmd_args.print:
        print (cmd)
    else:
        os.system(cmd)

    return

##############################################

runs = get_runs()

##############################################

num_runs = len(runs)
parallel_runs = 4

for run in range(0, num_runs, parallel_runs):
    threads = []
    for parallel_run in range( min(parallel_runs, num_runs - run)):
        args = runs[run + parallel_run]
        t = threading.Thread(target=run_command, args=(args,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        
