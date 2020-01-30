import numpy as np
import matplotlib.pylab as plt


def mysin():
    x = np.linspace(0, 2 * np.pi, num=150)
    y = np.cos(x)
    z = np.sin(x)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()


if __name__ == "__main__":
    mysin()
