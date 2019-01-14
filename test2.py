
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

T = 205e-9
dt = 1e-12
pulse_width = 10e-12
steps = int(T / dt) + 1
Ts = np.linspace(0., T, steps)

# Ts = np.linspace(0, 1, 500, endpoint=False)
wave = signal.square(2 * np.pi * (1. / pulse_width) * Ts)
plt.plot(Ts, wave)
plt.show()


