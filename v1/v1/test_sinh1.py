
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2., 2., 1000)
y = np.sinh(x / 0.25)

plt.plot(x, y)
plt.show()
