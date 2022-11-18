# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:06:31 2022
@author: Chad Kite

"""

import numpy as np
from fp2_invJ import gelim

'''
Uses provided equations (defined in fxyz, gxyz, and hxyz) and a vector of 3 numbers
to use as a start point (h0) to find a solution to the given system of equations
within the specified tolerance (tol) or up to the maximum # of iterations (imax).

*** Ensure fxyz, gxyz and hxyz match equations in fp_invJ ***
'''

# Define system of equations
def fxyz(n0): return n0[0]**2 + n0[1]**2 +n0[2]**2 - 10
def gxyz(n0): return n0[0] + 2*n0[1] - 2
def hxyz(n0): return n0[0] + 3*n0[2] - 9

# instantiate an instance of gelim for inverting Jacobian matrix
gelim = gelim()

# Use newton's method to solve a multivariable system of equations
def newton(fxyz,gxyz,hxyz,n0,tol,maxiter):
    itc = 0 # Set iteration count to 0
    h=.01 # Set offset to use in calculation of numerical derivatives
    
    n1=np.array([0,0,0]) # Create n1 array to store solutions from previous step
    fgh_n0 = [fxyz(n0), gxyz(n0), hxyz(n0)] # Get current solutions to equations
    
    # Print output header and first 2 rows of output from input values
    print('iter', '\tx0/fn0', '\t\t\t\ty0/gn0', '  \t\t\tz0/hn0')
    print(itc, '  ', n0[0], '\t\t\t\t\t', n0[1], '\t\t\t\t\t', n0[2])
    print(itc, ' ', fgh_n0[0], '\t\t\t\t\t', fgh_n0[1], '\t\t\t\t\t', fgh_n0[2])
    
    # Loop through newton until max norm of successive iteratates is < tol
    # or max iterations reached
    while ((max(abs(np.subtract(n0,n1)))>tol) & (itc < maxiter)):
        jinv = gelim.matinv(n0, h) # Invert Jacobian matrix
        try:
            n1 = n0 # store solutions from previous step
            n0 = n0 - np.matmul(jinv, fgh_n0) # Update current solutions
            fgh_n0 = [fxyz(n0), gxyz(n0), hxyz(n0)] # Get current solutions to equations
        except:
            raise Exception("f'(x) = 0 -> Cannot divide by zero")
        itc += 1 # increment iteration counter
       
        # Print current values of solutions and equation results
        print(itc, '\t%.15f'%n0[0], '\t%.15f'%n0[1], '\t%.15f'%n0[2])
        print(itc, '\t%.15f'%fgh_n0[0], '\t%.15f'%fgh_n0[1], '\t%.15f'%fgh_n0[2])
        
        # get equation results for updated set of solutions
        fgh_n0 = [fxyz(n0), gxyz(n0), hxyz(n0)]

    return itc, n0, fxyz(n0), gxyz(n0), hxyz(n0)

start_vals = [2,0,2]
tol=10e-6
imax=100
n0 = np.array(start_vals)
steps, est, fval, gval, hval = newton(fxyz,gxyz,hxyz,n0,tol,imax)
print('After',steps,'steps estimate is:',est)
print('f(xyz) =',fval)
print('g(xyz) =',gval)
print('h(xyz) =',hval)
