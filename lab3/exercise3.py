#!/usr/bin/inculde/python

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import math

t = 0
dt = 0.0001
t_max = 1.5
g = 9.81
B = 1.6*(10**-4)
D = 1*(10**-4)
m = 1.0472*(10**-8)

v = 12
theta = 1.76

v_x = v*math.cos(theta)
v_y = v*math.sin(theta)

Y = 0
X = 0
listY = []
listX = []
    
while Y >= 0:
    dv_x = -((B*D)/m)*v_x*dt
    dv_y = -g*dt - ((B*D)/m)*v_y*dt

    v_x = v_x + dv_x
    v_y = v_y + dv_y

    dY = v_y*dt
    dX = v_x*dt

    Y = Y + dY
    X = X + dX
    listY.append(Y)
    listX.append(-X) 

    t = t + dt

plt.plot(listX, listY, '.k', markersize = 0.7)
plt.show()
