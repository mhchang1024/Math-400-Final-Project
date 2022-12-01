# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:06:31 2022

@author: Charl
"""
# Find root of a function using Newton's method
import math
import matplotlib.pyplot as plt
from mpmath import *
import numpy as np

def f(x):
    return tanh(x)
 
def fp(x, h):
    return (f(x+h)-f(x-h)) / (2*h)

def hfun(x):
    return math.tan(x)

def newton(f,fp,x0,tol,maxiter):
    itc = 0
    fx0 = f(x0); 
    fpx0 = fp(x0, h)
    frat = fx0/fpx0
    print('iter  ', '\t\tx  ', '\t\t\t\tf(x) / fp(x)', '\t\t\t\ttan(x)')
    print(itc, '\t', '%.15f' % x0, ' \t', '%.15f' % frat, ' \t','%.15f' % hfun(x0))
    while (abs(f(x0)) > tol) & (itc < maxiter):
        try:
            x0 = x0 - fx0 / fpx0
        except:
            raise Exception("f'(x) = 0 -> Cannot divide by zero")
        itc += 1
        fx0 = f(x0); fpx0 = fp(x0,h); frat = fx0/fpx0
        print(itc, '\t', '%.15f' % x0, ' \t', '%.15f' % frat, ' \t','%.15f' % hfun(x0))
        yplot = x*hfun(x0)
        label = 'step ' + str(itc)
        line1, = plt.plot(x, yplot, label = label)
    plt.xlim(left=-5)
    plt.legend(loc='upper left')
    plt.show()
    return itc, x0

h=.1 # Set offset to use in calculation of numerical derivative

# Set interval for plotting function
x = np.linspace(0,10,50)

# set and format axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

steps, est = newton(f,fp,1.09,10e-12,50)
print('After',steps,'steps estimate is:',est)