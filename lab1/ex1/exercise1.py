#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return 1*x*x + 2*x -15

x_1 = 1
x_3 = 7
x_2 = 0.5*(x_1 + x_3)
min_val = 0.0001

if f(x_1) >= 0:
    print "Error: Choose x_1 such that f(x_1) < 0"
    
if f(x_3) <= 0:
    print "Eror: Choose x_3 such that f(x_3) > 0"

nsteps = 0

#while abs(f(x_2)) > min_val:
#    nsteps +=1
#
#    if f(x_2) > 0:
#        x_3 = x_2
#        x_2 = 0.5*(x_1 + x_3)
#    elif f(x_2) < 0:
#        x_1 = x_2
#        x_2 = 0.5*(x_1 + x_3)
#
#print " nsteps = %d" %int(nsteps)    
#print " x_1=%f\n x_2=%f\n x_3=%f\n f(x_2)=%f\n" %(float(x_1), float(x_2), float(x_3), float(f(x_2)))


listnsteps = []
listminvals = []
min_val2 = 0.001

while min_val2 < 1:
    x_1 = 1
    x_3 = 7
    x_2 = 0.5*(x_1 + x_3)
    nsteps +=1

    if f(x_2) > 0:
        x_3 = x_2
        x_2 = 0.5*(x_1 + x_3)
    elif f(x_2) < 0:
        x_1 = x_2
        x_2 = 0.5*(x_1 + x_3)
        
    listnsteps.append(nsteps)
    listminvals.append(math.log10(min_val2))
    min_val2 += 0.001
    
x = np.arange(-2.0, 8.0, 0.1)    
#plt.plot(x, f(x))
#plt.plot(x_2, f(x_2), 'r^')
plt.scatter(listnsteps, listminvals)
plt.axhline(y=0)
plt.axvline(x=0)
plt.show()

    
