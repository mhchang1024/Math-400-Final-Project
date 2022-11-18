# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:06:31 2022

@author: Charl
"""
# Find root of a function using Secant method
import math
import matplotlib.pyplot as plt
from mpmath import *
import numpy as np

def f(x):
    return tanh(x)

def h(x):
    return math.tan(x)

def secant(f,x0,tol,maxiter):
    x1 = x0 + .01
    x2 = 0.0
    itc = 0
    fx0 = f(x0)
    fx1 = f(x1);
    print('iteration  ', '\tx  ', '\t\t\t\t\ttan(x)')
    while (abs(f(x1)) > tol) & (itc < maxiter):
        try:
            x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        except:
            raise Exception("f(x1) - f(x0) = 0. Cannot divide by 0")
        x0 = x1; fx0 = fx1
        x1 = x2; fx1 = f(x2)
        itc += 1
        print(itc, '\t\t', '%.18f' % x1, '\t', '%.18f' % h(x1))
        yplot = x*h(x0)
        label = 'step ' + str(itc)
        line1, = plt.plot(x, yplot, label = label)
    plt.xlim(left=-5) 
    plt.legend(loc='upper left')
    plt.show()
    return itc, x1

# Set interval for plotting function
x = np.linspace(0,10,50)

# set and format axes
fig = plt.figure()
plt.rcParams["figure.figsize"] = [5.0, 4.0]
plt.rcParams["figure.autolayout"] = False
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

steps, est = secant(f,1.09,1e-30,20)
print('After',steps,'steps estimate is:',est)