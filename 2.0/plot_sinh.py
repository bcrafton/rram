
import numpy as np
import matplotlib.pyplot as plt
from rram import rram

x = np.linspace(0., 500, 100)
y = np.sinh(x)
plt.plot(x, y)
plt.show()

