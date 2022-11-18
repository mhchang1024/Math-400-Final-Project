# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:58:25 2022

@author: Charl
"""
# Class for finding a root using the bisection method   

from mpmath import *

'''
Perform bisection on input from main until width of interval meets the given
requirement for switching to Newton's method or max iterations exceeded.
'''

# Use bisection to decrease the length of the interval in which the root exists
class bsct: 
   def bisection(self,f,a,b,width,itc,itmax):
        print('Begin bisecting...')
        # set/get initial values
        x_new = 0.0
        a_val = f(a)
        b_val = f(b)
        # check that f(a) and f(b) have opposite signs
        if (a_val * b_val < 0):
            # loop until interval is smaller than width or loop exceeds max iterations
            while ((b-a > width) & (itc < itmax)):
                # get values for current step
                x_new = (a+b) / 2
                fx = f(x_new)
                itc += 1 # increment iteration counter
                # Check to see whether a or b should be replaced with current estimate
                if (fx * f(a) < 0):
                    b = x_new
                    b_val = fx
                else:
                    a = x_new
                    a_val = fx
                print(itc,": The root is in the interval",a,"and",b)
        else:
            print ("f(a) and f(b) have the same sign")
        return itc, a, b
