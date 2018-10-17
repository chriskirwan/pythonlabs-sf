#!/usr/bin/python

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import math

def V(s):
    return 1090*np.exp(-30.303*s) - 1.44*(1/s)

def C(s):
    return -(33030.3)*np.exp(-30.303*s) + 1.44*(1/(s*s))

def X(s):
    return (1000918.274)*np.exp(-30.303*s) - 2.88*(1/(s*s*s))

x1 = 0.2
nsteps = 0
min_val = 0.00001

while abs(C(x1)) > min_val:
    nsteps += 1
    x1 = x1 - float(C(x1))/float(X(x1))

print " nsteps: %d\n x1: %f\n f(x1): %f\n" %(nsteps, float(x1), float(V(x1)))

x = np.arange(0.01, 1.00, 0.01)
plt.ylim(-10, 20)
plt.plot(x, V(x))
plt.plot(x, C(x), 'r')
plt.axhline(y=0)
plt.axvline(x=0)
plt.show()

