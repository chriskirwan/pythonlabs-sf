#!/usr/bin/python

import matplotlib.pylab as plt
import numpy as np

result = []

def fib(n): 
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result

fib_series = fib(10)

print fib_series
print '\n'.join(map(str, fib_series))
