#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return 1*x*x +2*x - 15

def g(x):
    return 1*x +2

x1 = 1
min_val = 0.0001
nsteps = 0

while abs(f(x1)) > min_val:
    nsteps += 1
    x1 = x1 - float(f(x1))/float(g(x1))

print " nsteps: %d\n x1: %f\n f(x1): %f\n" %(nsteps, float(x1), float(f(x1)))

listnsteps = []
listminvals = []
min_val2 = 0.001

while min_val2 < 1:
    x1 = 1
    nsteps +=1
    x1 = x1 - float(f(x1))/float(g(x1))
     
    listnsteps.append(nsteps)
    listminvals.append(math.log10(min_val2))
    min_val2 += 0.001


x = np.arange(-10.0, 10.0, 0.1)
#plt.plot(x, f(x), x, g(x), 'g')
#plt.plot(x1, f(x1), 'r^')
plt.scatter(listnsteps, listminvals)
plt.axhline(y=0)
plt.axvline(x=0)
plt.show()
