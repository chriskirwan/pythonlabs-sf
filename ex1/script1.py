#!/usr/bin/python

import matplotlib.pylab as plt
import numpy as np

a = 1
b = 1 
c = -6 

x = np.arange(-5.0, 5.0, 2.0)
plt.plot(x, a*x*x + b*x +c)
plt.plot(x, 0.0*x)
plt.show()