#include /usr/bin/python

from __future__ import division

import math
import matplotlib.pyplot as plt
import numpy as np

#----------------------------#
#----------------------------#
def simpson(f,a,b,n):
    h = (b-a)/n
    s = f(a) + f(b)

    for i in range(1,n,2):
        s += 4*f(a+ i*h)
    for i in range(2,n-1,2):
        s += 2 * f(a +i*h)

    return s*h/3
#----------------------------#
#----------------------------#

def a_0(f,a,b,n):
  return (1/b)*simpson(f,a,b,n)

def func(x):
    return math.sin(x)

print a_0(func, 0, 2*math.pi, 50)
print '\n'

#----------------------------#
#----------------------------#

def a_k(f,a,b,n):
    return (2/b)*simpson(f,a,b,n)

lista_k = []
listofa_k = []
for i in range(1, 10):
    lista_k.append(i)

for i in lista_k: 
    def func_a_k(x):
        return math.sin(x)*np.cos(i*x)
    listofa_k.append(a_k(func_a_k, 0, 2*math.pi, 50))
    print a_k(func_a_k, 0, 2*math.pi, 10)
    
print '\n'
#----------------------------#
#----------------------------#
    
def b_k(f,a,b,n):
    return (2/b)*simpson(f,a,b,n)

listb_k = []
listofb_k = []
for i in range(1, 10):
    listb_k.append(i)

for i in listb_k: 
    def func_b_k(x):
        return math.sin(x)*np.sin(i*x)
    listofb_k.append(b_k(func_b_k, 0, 2*math.pi, 50))
    print b_k(func_b_k, 0, 2*math.pi, 50) 
#----------------------------#

listxplot = list(range(1,10))
plt.scatter(listxplot, listofa_k)
plt.scatter(listxplot, listofb_k, c = 'g')
                 
#x = np.arange(0, 4*math.pi, 0.001)
#plt.plot(x, func(x), '.k')
#plt.ylim(-1.1, 1.1)
#plt.xlim(0, 12)
plt.show()


