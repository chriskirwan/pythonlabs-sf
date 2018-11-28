#include /usr/bin/python

from __future__ import division

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal 


N_max = 60
n_odds = np.arange(1,N_max,2)
xs = np.arange(0,2*math.pi,0.001)
ys = []
for x in xs:
    sum_terms = []
    for n_odd in n_odds:
        frac_term = 2/(4*n_odd*np.pi)
        sin_term = np.sin(n_odd*x)
        sum_term = frac_term*sin_term
        sum_terms.append(sum_term)

    y = 2*sum(sum_terms)
    ys.append(y)

plt.plot(xs, ys)
plt.plot(xs, (1/4)*signal.square(xs))
plt.show()
