#!/usr/bin/inculde/python

import matplotlib.pyplot as plt
import numpy as np
import math

B = 0.00016
C = 0.25

def f(V):
    return B*V

def g(V):
    return C*V*V

x = np.arange(-0.001, 0.001, 0.000001)
plt.plot(x, f(x), '.r', markersize = 0.7)
plt.plot(x, g(x), '.g', markersize = 0.7)

plt.show()

