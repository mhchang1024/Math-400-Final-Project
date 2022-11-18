# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:10:38 2022
@author: Charl
"""
from mpmath import *
from fp_bsct import bsct
from fp_nwtn import nwtn

mybisect = bsct()
mynewt = nwtn()

def root(f, fp, a, b, width, tol, imax):
    # end loop when tol met or imax met
    x0 = (b+a)/2; itc=0
    if (f(x0)==0): print('The given function evaluates to 0 at the center of the given end points:', x0)
    while ((abs(f(x0)) > tol) & (itc < imax)):    
        # loop through bisection and newton
        # if width not met, bisect
        if (b-a > width):
            itc, a, b = mybisect.bisection(f,a,b,width,itc,imax)
            x0 = (b+a)/2
            print('After', itc,'steps the root is in the interval',a,'and',b)
            print('The estimate of the root is', x0)
            print('The width of the interval is', abs(b-a))
        # if width met, newton
        else: print('Interval between a (', a,') and b (', b,') is not greater than the specified width (', width,').')
        if ((abs(f(x0)) > tol) & (itc < imax)):
            itc, x0 = mynewt.newton(f,fp,a,b,tol,itc,imax)
            print('After', itc,'steps estimate is:', x0)
            # reduce width if newton has diverged from root
            if (not(a < x0 < b)):
                print('Estimate is not in the specified interval. Reducing width by 1/10.')
                width = width / 10
    return
     
# Define function for which to approximate root
f = lambda x: tanh(x)
# The derivative of f
fp = lambda x: sech(x)**2

# f -> the function for which a root will be approximated
# fp -> the derivative of f
# a -> the lower end point of the starting interval
# b -> the upper end point of the starting interval
# width -> the interval width at which bisection will end and newtoning will begin (positive #)
# tol -> the acceptable difference between f(x0) and 0 (positive #)
# imax -> the maximum number of iterations allowed (bisection and newton combined)
root(f, fp, -10, 11, .1, 10e-10, 20)
