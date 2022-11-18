"""
Created on Thu Sep  8 12:06:31 2022
@author: Chad Kite

"""

import copy
import numpy as np

'''
Takes a 3 number vector, n0, and an offset, h, and uses the given partial
numerical derivatives to calculate the Jacobian matrix, then uses Gaussian
Elimination with partial pivoting to reduce the matrix into upper diagonal
form and solves for the inverse of the Jacobian matrix using back substitution.

*** Ensure fxyz, gxyz and hxyz match equations in fp_newton_multivariable ***
'''

# Get inverse of 3x3 matrix by GE with PP to UT then back-substitution
class gelim:
    def matinv(self,n0,h):
        # Get jacobian matrix
        jmat = np.array([[fpx(n0,h), fpy(n0,h), fpz(n0,h)],
                        [gpx(n0,h), gpy(n0,h), gpz(n0,h)],
                        [hpx(n0,h), hpy(n0,h), hpz(n0,h)]])
        # Create identity matrix
        idmat = np.array([[1.0,0.0,0.0],
                         [0.0,1.0,0.0],
                         [0.0,0.0,1.0]])
        # Add identity matrix to right side of jacobian
        jinv = np.concatenate((jmat,idmat), axis=1)
        
        # check to make sure jacobian matrix is invertible
        if (np.linalg.det(jmat) == 0):
            print('Determinant of J is 0.')
            return
        
        # Iterate through matrix by column
        for i in range(2):    
            # identify pivot in working column
            col_i = abs(jinv[0+i:3,i]) # isolate working column (i) 
            pivot=max(col_i); # get position of pivot in working column
            t,=np.where(col_i == pivot)[0]+i; #find pivot i and its index  
            # transpose rows to put pivot into correct position
            temp1 = jinv[i,:].copy()
            temp2 = jinv[t,:].copy()
            jinv[i] = temp2
            jinv[t] = temp1
    
            # Iterate through matrix by rows below diagonal 
            for j in range(2-i):  
                try:
                    mult = jinv[2-j,i] / jinv[i,i] # get multiplier 
                except:
                    raise Exception("Cannot divide by zero")
                jinv[2-j,]=jinv[2-j,]-mult*jinv[i,] # conduct row operation
            
        # use back substitution to solve inverse
        for i in range(2):
            for j in range(2-i):
                try:
                    mult = jinv[j, 2-i] / jinv[2-i,2-i] # get multiplier
                except:
                    raise Exception("Cannot divide by zero")
                jinv[j,] = jinv[j,] - mult * jinv[2-i,]  # conduct row operation
                        
        for i in range(3):
            jinv[i,] = jinv[i,] / jinv[i,i] # reduce pivot values to 1
            
        # return inverse portion of matrix
        return jinv[:,3:6]

# Define equations and partial numerical derivatives
def fxyz(n0): return n0[0]**2 + n0[1]**2 +n0[2]**2 - 10
def gxyz(n0): return n0[0] + 2*n0[1] - 2
def hxyz(n0): return n0[0] + 3*n0[2] - 9

def fpx(n0,h): return (fxyz(n0+[h,0,0])-fxyz(n0-[h,0,0])) / (2*h)
def fpy(n0,h): return (fxyz(n0+[0,h,0])-fxyz(n0-[0,h,0])) / (2*h)
def fpz(n0,h): return (fxyz(n0+[0,0,h])-fxyz(n0-[0,0,h])) / (2*h)
     
def gpx(n0,h): return (gxyz(n0+[h,0,0])-gxyz(n0-[h,0,0])) / (2*h)
def gpy(n0,h): return (gxyz(n0+[0,h,0])-gxyz(n0-[0,h,0])) / (2*h)
def gpz(n0,h): return 0

def hpx(n0,h): return (hxyz(n0+[h,0,0])-hxyz(n0-[h,0,0])) / (2*h)
def hpy(n0,h): return 0
def hpz(n0,h): return (hxyz(n0+[0,0,h])-hxyz(n0-[0,0,h])) / (2*h)

