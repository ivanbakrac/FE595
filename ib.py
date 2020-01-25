import numpy as np
import matplotlib.pylab as plt
x = np.linspace(0, 2*np.pi)
y = np.cos(x)
z = np.sin(x)
plt.plot(x,y)
plt.plot(x,z)
plt.show()