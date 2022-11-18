import copy
import numpy as np


# Get inverse of 3x3 matrix by GE with PP to UT then back-substitution
class gelim:
    def matinv(self,n0,h):
        jmat = np.array([[fpx(n0,h), fpy(n0,h), fpz(n0,h)],
                        [gpx(n0,h), gpy(n0,h), gpz(n0,h)],
                        [hpx(n0,h), hpy(n0,h), hpz(n0,h)]])
        idmat = np.array([[1.0,0.0,0.0],
                         [0.0,1.0,0.0],
                         [0.0,0.0,1.0]])
        jinv = np.concatenate((jmat,idmat), axis=1)
        if (np.linalg.det(jmat) == 0):
            print('Determinant of J is 0.')
            return
        
        # Identify pivot
        for i in range(2):    
            col_i = abs(jinv[0+i:3,i]) #isolate column i 
            pivot=max(col_i);
            t,=np.where(col_i == pivot)[0]+i; #find pivot i and its index  
            # transpose rows
            temp1 = jinv[i,:].copy()
            temp2 = jinv[t,:].copy()
            jinv[i] = temp2
            jinv[t] = temp1
    
            # Get multiplier and reduce remaining row(s) below diagonal
            for j in range(2-i):  
                try:
                    mult = jinv[2-j,i] / jinv[i,i]
                except:
                    raise Exception("Cannot divide by zero")
                jinv[2-j,]=jinv[2-j,]-mult*jinv[i,]
            
        ### implement back substitution
        for i in range(2):
            for j in range(2-i):
                try:
                    mult = jinv[j, 2-i] / jinv[2-i,2-i]
                except:
                    raise Exception("Cannot divide by zero")
                jinv[j,] = jinv[j,] - mult * jinv[2-i,] 
                        
        for i in range(3):
            jinv[i,] = jinv[i,] / jinv[i,i] 
            
        return jinv[:,3:6]

def fxyz(n0): return n0[0]**2 + n0[1]**2 +n0[2]**2 - 10
def fpx(n0,h): return (fxyz(n0+[h,0,0])-fxyz(n0-[h,0,0])) / (2*h)
def fpy(n0,h): return (fxyz(n0+[0,h,0])-fxyz(n0-[0,h,0])) / (2*h)
def fpz(n0,h): return (fxyz(n0+[0,0,h])-fxyz(n0-[0,0,h])) / (2*h)
     
def gxyz(n0): return n0[0] + 2*n0[1] - 2
def gpx(n0,h): return (gxyz(n0+[h,0,0])-gxyz(n0-[h,0,0])) / (2*h)
def gpy(n0,h): return (gxyz(n0+[0,h,0])-gxyz(n0-[0,h,0])) / (2*h)
def gpz(n0,h): return 0

def hxyz(n0): return n0[0] + 3*n0[2] - 9
def hpx(n0,h): return (hxyz(n0+[h,0,0])-hxyz(n0-[h,0,0])) / (2*h)
def hpy(n0,h): return 0
def hpz(n0,h): return (hxyz(n0+[0,0,h])-hxyz(n0-[0,0,h])) / (2*h)

#-------Example-------------------------
#b = np.array([[1.0],[7.0],[0.0],[3]])
#A = np.array([[1.0, -2.0, -4.0, -3.0],[2.0, -7.0, -7.0, 6.0],[-1.0, 2.0, 6.0, 4.0],[-4.0, -1.0, 9.0, 8.0]])

# h=.1
#n0=np.array([2, 0, 2])
# y=gelim.matinv(n0, h)
#x=part_piv_ge(A.copy(),b.copy())
#print(y)
