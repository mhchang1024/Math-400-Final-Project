# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:06:31 2022
@author: Charl
"""
# Find root of a 3 variable function using Newton's method
import numpy as np
from fp_invJ import gelim

def fxyz(n0): return n0[0]**2 + n0[1]**2 +n0[2]**2 - 10
     
def gxyz(n0): return n0[0] + 2*n0[1] - 2

def hxyz(n0): return n0[0] + 3*n0[2] - 9

gelim = gelim()

#def matinv(n0,h):
#    jmat = np.array([[fpx(n0,h), fpy(n0,h), fpz(n0,h)],
#                    [gpx(n0,h), gpy(n0,h), gpz(n0,h)],
#                    [hpx(n0,h), hpy(n0,h), hpz(n0,h)]])
#    if (np.linalg.det(jmat) == 0):
#        print('Determinant of J is 0.')
#    try:
#        jinv = np.linalg.inv(jmat)
#    except:
#        raise Exception("Could not calculate J inverse")
#    return jinv

def newton(fxyz,gxyz,hxyz,n0,tol,maxiter):
    itc = 0
    h=.01
    jinv = gelim.matinv(n0, h)
    n1=np.array([0,0,0])
    fgh_n0 = [fxyz(n0), gxyz(n0), hxyz(n0)]
    # print(jinv)
    # print(fgh_n0)
    # print(np.matmul(jinv, fgh_n0))
    print('iter', '\tx0/fn0', '\t\t\t\ty0/gn0', '  \t\t\tz0/hn0')
    print(itc, '  ', n0[0], '\t\t\t\t\t', n0[1], '\t\t\t\t\t', n0[2])
    print(itc, ' ', fgh_n0[0], '\t\t\t\t\t', fgh_n0[1], '\t\t\t\t\t', fgh_n0[2])
    while ((max(abs(np.subtract(n0,n1)))>tol) & (itc < maxiter)):
        try:
            n1 = n0
            n0 = n0 - np.matmul(jinv, fgh_n0)
            fgh_n0 = [fxyz(n0), gxyz(n0), hxyz(n0)]
        except:
            raise Exception("f'(x) = 0 -> Cannot divide by zero")
        itc += 1
        print(itc, '\t%.15f'%n0[0], '\t%.15f'%n0[1], '\t%.15f'%n0[2])
        print(itc, '\t%.15f'%fgh_n0[0], '\t%.15f'%fgh_n0[1], '\t%.15f'%fgh_n0[2])
        jinv = gelim.matinv(n0, h)
        fgh_n0 = [fxyz(n0), gxyz(n0), hxyz(n0)]
        # print(jinv)
        # print(fgh_n0)
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
