
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 2 * np.pi, 1000)
y = np.sinh(x)

plt.plot(x, y)
plt.show()
