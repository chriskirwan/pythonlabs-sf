#!/usr/bin/python

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import math

def V(s):
    return 1090*math.exp(-s/0.033) - 1.44*(1/s)

x = np.arange(0.01, 1.00, 0.01)
listx = np.exp(x)

plt.plot(1090/(listx/0.033) -1.44/x)
plt.show()

