#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return x*x + 2*x -15

def g(x):
    return x + 2

x1 = 1
min_val = 0.0001
nsteps = 0

while abs(f(x1)) > min_val:
    nsteps += 1
    x1 = x1 - float(f(x1))/float(g(x1))

print " nsteps: %d\n x1: %f\n f(x1): %f\n" %(nsteps, float(x1), float(f(x1)))


plt.plot(math.log10(nsteps), min_val, 'b^')        
plt.show()
