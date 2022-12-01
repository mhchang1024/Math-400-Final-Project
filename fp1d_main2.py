# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:10:38 2022
@author: Charl
"""
from mpmath import *
from fp1d_bsct import bsct
from fp1d_nwtn2 import nwtn

'''
Use bisection and Newton's method in turn to find the root of a given equation.
Must define:
    f -> the function for which a root will be found
    fp -> the derivative of the function (f)
    a -> lower end of interval for start of bisection
    b -> upper end of interval for start of bisection
    width -> width of interval at which to switch from bisection to Newton's method
    tol -> the desired tolerance for the root
    imax -> the maximum # of iterations to complete
'''

# Instatiate instances of bsct and nwtn
mybisect = bsct()
mynewt = nwtn()

# find root of given equation
def root(f, fp, a, b, width, tol, imax):
    # Set start value for root in bisection based on midpoint of provided interval
    x0 = (b+a)/2; itc=0
    # Check to see if calculations must be done
    if (f(x0)==0): print('The given function evaluates to 0 at the center of the given end points:', x0)
    # Create loop to cycle between bisection and Newton's method as needed until
    # conditions are met
    while ((abs(f(x0)) > tol) & (itc < imax)):    
        # if width not met, bisect
        if (b-a > width):
            itc, a, b = mybisect.bisection(f,a,b,width,itc,imax) # Call bisection
            x0 = (b+a)/2 # set new estimate of root
            # Output results of bisection
            print('After', itc,'steps the root is in the interval',a,'and',b)
            print('The estimate of the root is', x0)
            print('The width of the interval is', abs(b-a))
        # if width met, switch to Newton's method
        else: print('Interval between a (', a,') and b (', b,') is not greater than the specified width (', width,').')
        # check to see if Newton's method is necessary
        if ((abs(f(x0)) > tol) & (itc < imax)):
            itc, x0 = mynewt.newton(f,a,b,tol,itc,imax) # Call Newton's method
            # Output results of Newton's method
            print('After', itc,'steps estimate is:', x0)
            # reduce width if newton has diverged from root
            if (not(a < x0 < b)):
                print('Estimate is not in the specified interval. Reducing width by 1/10.')
                width = width / 10
    return
     
# Define function for which to approximate root
f = lambda x: tanh(x)
# f and the derivative of f must be updated in fp1d_nwtn.py

# f -> the function for which a root will be approximated
# fp -> the derivative of f
# a -> the lower end point of the starting interval
# b -> the upper end point of the starting interval
# width -> the interval width at which bisection will end and newtoning will begin (positive #)
# tol -> the acceptable difference between f(x0) and 0 (positive #)
# imax -> the maximum number of iterations allowed (bisection and newton combined)
root(f, fp, -10, 15, .1, 10e-10, 20)
