
import numpy as np
import matplotlib.pyplot as plt

def pulse(T, t1, t2, v1, v2):
    N = T // (t1 + t2)
    R = T % (t1 + t2)
    assert (R == 0)
    V1 = np.ones(shape=t1) * v1
    V2 = np.ones(shape=t2) * v2
    V = np.concatenate((V1, V2))
    V = np.tile(V.reshape(1, -1), (N, 1)).flatten()
    return V

# T = np.arange(100)
# V = pulse(100, 4, 6, 0, 1)
# plt.plot(T, V)
# plt.savefig('img.png')

    
