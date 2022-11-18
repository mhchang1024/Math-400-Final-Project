# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:58:25 2022

@author: Charl
"""
# Find a root using the bisection method   
import math
import matplotlib.pyplot as plt
from mpmath import *
import numpy as np

def bisect(f,a,b,width,itmax):
    x = 1.0
    x_new = 0.0
    itc = 0
    a_val = f(a)
    b_val = f(b)
    ### check that f(a) and f(b) have opposite signs
    if (a_val * b_val < 0):
        ### loop bisection until error < delta or loop exceeds max iterations
        while ((b-a > width) & (itc < itmax)):
            x_new = (a+b) / 2
            fx = f(x_new)
            itc += 1
            # print (itc, a, a_val, b, b_val, x_new, x)
            if (fx * f(a) < 0):
                b = x_new
                b_val = fx
            else:
                a = x_new
                a_val = fx
            # print(b-a-delta)
            print(itc,": The root is in the interval",a,"and",b)
            yplot = x*h(x_new)
            label = 'step ' + str(itc)
            line1, = plt.plot(x, yplot, label = label)
        plt.legend(loc='upper left')
        plt.show()
    else:
        print ("f(a) and f(b) have the same sign")
    return itc, a, b

# Define function
def f(x):
    return tanh(x)

def h(x):
    return math.tan(x)

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

steps, li, ui = bisect(f,-5,3,10e-20,50)
print('After', steps,'steps the root is in the interval',li,'and',ui)
print('The estimate of the root is',(ui+li)/2)
print('The width of the interval is',abs(ui-li))