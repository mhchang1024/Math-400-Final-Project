# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 11:58:25 2022

@author: Charl
"""
# Class for finding a root using the bisection method   

from mpmath import *

class bsct: 
   def bisection(self,f,a,b,width,itc,itmax):
        print('Begin bisecting...')
        x_new = 0.0
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
        else:
            print ("f(a) and f(b) have the same sign")
        return itc, a, b
