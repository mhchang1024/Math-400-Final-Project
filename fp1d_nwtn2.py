# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:06:31 2022

@author: Charl
"""
# Class for finding root of a function using Newton's method

import math
import matplotlib.pyplot as plt
from mpmath import *
import numpy as np

'''
Perform Newton's method on input from main until desired tolerance or maximum
iterations met, or specified width switching between bisection and Newton's method
is exceeded. 
x -> interval for plotting the progress of Newton's method
'''

# Use Newton's method to refine the estimate of the root provided
class nwtn:
    def newton(self,f,a,b,tol,itc,maxiter):
        print('Begin newtoning...')
        # get initial values
        x0 = (b+a)/2; fx0 = f(x0); fpx0 = fp(x0); frat = fx0/fpx0
        # create output title and print current estimate and result
        print('iter  ', '\t\tx  ', '\t\t\t\tf(x) / fp(x)', '\t\t\t\ttan(x)')
        print(itc, '\t', '%.15f' % x0, ' \t', '%.15f' % frat, ' \t','%.15f' % f(x0))
        # create loop to perform Newton's method until tol met, estimate leaves
        # bounds provide, or max iterations exceeded
        while (abs(f(x0)) > tol) & (a < x0 < b) & (itc < maxiter):
            # Get next estimate of root
            try:
                x0 = x0 - fx0 / fpx0
            except:
                raise Exception("f'(x) = 0 -> Cannot divide by zero")
            itc += 1    # increment iteration count
            fx0 = f(x0); fpx0 = fp(x0); frat = fx0/fpx0     # get current values
            # Output current estimate and result
            print(itc, '\t', '%.15f' % x0, ' \t', '%.15f' % frat, ' \t','%.15f' % f(x0))
            # create plot of progress toward root
            yplot = x*f(x0)
            label = 'step ' + str(itc)
            line1, = plt.plot(x, yplot, label = label)
        plt.xlim(left=-5)
        plt.legend(loc='upper left')
        plt.show()
        return itc, x0

f = lambda x: tanh(x)
h=.01 # Set offset to use in calculation of numerical derivatives
fp = lambda x: (f(x+h)-f(x-h)) / (2*h)

# Set interval for plotting function
x = np.linspace(0,5,10)

# set and format axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')