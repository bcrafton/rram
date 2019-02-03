
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500, endpoint=False)
wave = signal.square(2 * np.pi * 5 * t)
plt.plot(t, wave)
plt.show()


