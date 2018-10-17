#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math

theta = 3
omega = 0.0
t = 0.0
dt = 0.01
#nsteps = 0

def f(theta, omega, t):
    k = 0.5
    phi = 0.66667
    A = 0.0
    
    return -math.sin(theta) - k*(omega) + A*math.cos(phi*t)

for i in range(3000):
    k1a = dt*omega
    k1b = dt*(f(theta, omega, t))
    k2a = dt*(omega + float(k1b)/2)
    k2b = dt*(f(theta + float(k1a)/2, omega + float(k1b)/2, t + dt/2))
    k3a = dt*(omega + float(k2b)/2)
    k3b = dt*(f(theta + float(k2a)/2, omega + float(k2b)/2, t + dt/2))
    k4a = dt*(omega + float(k3b)/2)
    k4b = dt*(f(theta +k3a, omega +k3b, t + dt))
    t = t + dt

    theta = theta + float(k1a + 2*k2a + 2*k3a + k4a)/6
    omega = omega + float(k1b + 2*k2b + 2*k3b + k4b)/6
    plt.plot(t, theta, '^g')
    plt.plot(t, omega, '^r')

plt.show()
