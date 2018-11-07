#!/usr/bin/inculde/python

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import math

t = 0
dt = 0.01
t_max = 5

V_num = 0
V_anl = 0

g = 9.81
B = 1.6*(10**-4)
D = 1*(10**-4)
m = 1.0472*(10**-8)


while t < t_max:
    
    dV_num = -g*dt - (float(B*D)/float(m))*V_num*dt
    V_num = V_num + dV_num

    V_anl = ((m*g)/(B*D))*(math.exp((-(B*D)*t)/(m))-1)
    
    V_err = V_anl - V_num
    
    t = t + dt
    
    #plt.plot(t, V_num, '.k', markersize = 0.7)
    #plt.plot(t, V_anl, '.b', markersize = 0.7)
    #plt.plot(t, -6.411, '.r', markersize = 0.7)
    plt.plot(t, V_err, '.k' , markersize = 0.7)

plt.show()
