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

def h(x):
    return math.tan(x)

class nwtn:
    def newton(self,f,a,b,tol,itc,maxiter):
        print('Begin newtoning...')
        x0 = (b+a)/2; h=x0/10; fx0 = f(x0)
        fpx0 = (f(x0+h)-f(x0-h)) / (2*h)
        frat = fx0/fpx0; hx0 = math.tan(x0)
        print('iter  ', '\t\tx  ', '\t\t\t\tf(x) / fp(x)', '\t\t\t\ttan(x)')
        print(itc, '\t', '%.15f' % x0, ' \t', '%.15f' % frat, ' \t','%.15f' % hx0)
        while (abs(f(x0)) > tol) & (a < x0 < b) & (itc < maxiter):
            try:
                x0 = x0 - fx0 / fpx0
            except:
                raise Exception("f'(x) = 0 -> Cannot divide by zero")
            itc += 1
            h=x0/10; fx0 = f(x0); fpx0 = (f(x0+h)-f(x0-h)) / (2*h)
            frat = fx0/fpx0; hx0 = math.tan(x0)
            print(itc, '\t', '%.15f' % x0, ' \t', '%.15f' % frat, ' \t','%.15f' % hx0)
            yplot = x*hx0
            label = 'step ' + str(itc)
            line1, = plt.plot(x, yplot, label = label)
        plt.xlim(left=-5)
        plt.legend(loc='upper left')
        plt.show()
        return itc, x0


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