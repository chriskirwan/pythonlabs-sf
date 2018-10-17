#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math

theta = 1
omega = 0.0
t = 0.0
dt = 0.01
nsteps = 0

def f(theta, omega, t):
    k = 0.0
    phi = 0.66667
    A = 0.0
    
    return -math.sin(theta) - k*(omega) + A*math.cos(phi*t)

def g(theta, omega, t):
    k = 0.0
    phi = 0.66667
    A = 0.0
    
    return -(theta) - k*(omega) + A*math.cos(phi*t)

print " Theta: %f\n Omega: %f\n t: %f\n" %(float(theta), float(omega), float(t))

for i in range(3000): 
    k1a = dt*omega
    k1b = dt*(f(theta, omega, t))
    k2a = dt*(omega + k1b)
    k2b = dt*(f(theta + k1a, omega + k1b, t + dt))
    theta = theta + float((k1a + k2a))/2
    omega = omega + float((k1b + k2b))/2
    t = t + dt


    nsteps = nsteps + 1
    plt.plot(nsteps, theta, '^g')
    #plt.plot(nsteps, omega, '^r')

theta = 1
omega = 0.0
t = 0.0
dt = 0.01
nsteps = 0

for i in range(3000):
    k1a = dt*omega
    k1b = dt*(g(theta, omega, t))
    k2a = dt*(omega + k1b)
    k2b = dt*(g(theta + k1a, omega + k1b, t + dt))
    theta = theta + float((k1a + k2a))/2
    omega = omega + float((k1b + k2b))/2
    t = t + dt


    nsteps = nsteps + 1
    plt.plot(nsteps, theta, '^g')
    #plt.plot(nsteps, omega, '^r')


plt.show()
