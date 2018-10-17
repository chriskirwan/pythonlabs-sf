#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return 2*x*x - 6*x - 11

x_1 = -1
x_3 = -3
x_2 = 0.5*(x_1 + x_3)
min_val = 0.0001

if f(x_1) >= 0:
    print "Error: Choose x_1 such that f(x_1) < 0"
    
if f(x_3) <= 0:
    print "Eror: Choose x_3 such that f(x_3) > 0"
    
while abs(f(x_2)) > min_val:

    if f(x_2) > 0:
        x_3 = x_2
        x_2 = 0.5*(x_1 + x_3)
    elif f(x_2) < 0:
        x_1 = x_2
        x_2 = 0.5*(x_1 + x_3)
    
print "x_1=%f x_2=%f x_3=%f f(x_2)=%f" %(float(x_1), float(x_2), float(x_3), float(f(x_2)))

x = np.arange(-2.0, 8.0, 0.1)    
plt.plot(x, f(x))
plt.plot(x_2, f(x_2), 'r^')
plt.axhline(y=0)
plt.axvline(x=0)
plt.show()

    
