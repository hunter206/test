import numpy as np
import scipy

YAW =30*np.pi/180
ROLL = 20*np.pi/180
PITCH = 40*np.pi/180

L = 1;
A_b = np.matrix([0,-L/2.0,0]).T
B_b = np.matrix([0,L/2.0,0]).T
print('B_b=')
print(B_b)
Cbc1 = np.matrix([[0,0,1],
		  [-1,0,0],
		  [0,-1,0]])
Cbc2 = np.matrix([[0,0,1],
		  [1,0,0],
		  [0,1,0]])
C_n = np.matrix([0,0,0]).T
D_n = np.matrix([1,30,2]).T
M_n = np.matrix([3,10,-4]).T
lBA_b = np.matrix([0,-1,0]).T

R3 = np.matrix([[np.cos(YAW),-np.sin(YAW),0],
		[np.sin(YAW),np.cos(YAW),0],
		[0,0,1]])
R2 = np.matrix([[np.cos(ROLL),0,np.sin(ROLL)],
		[0,1,0],
		[-np.sin(ROLL),0,np.cos(ROLL)]])
R1 = np.matrix([[1,0,0],
		[0,np.cos(PITCH),-np.sin(PITCH)],
		[0,np.sin(PITCH),np.cos(PITCH)]])
Cbn = (R2*R1*R3).I

Tbn = M_n

A_n = Cbn*A_b + Tbn
print('A_n=')
print(A_n)
B_n = Cbn*B_b + Tbn
print('B_n=')
print(B_n)

#M_n = np.matrix([3,10,-4]).T
eAC_n = (C_n - A_n)/np.linalg.norm(C_n - A_n)
eCD_n = (D_n - C_n)/np.linalg.norm(D_n - C_n)
eDB_n = (B_n - D_n)/np.linalg.norm(B_n - D_n)
lBA_n = Cbn*lBA_b
eBA_n = lBA_n/np.linalg.norm(lBA_n)

print('eAC_n=')
print(eAC_n)
print('eCD_n=')
print(eCD_n)
print('eDB_n=')
print(eDB_n)
print('eBA_n=')
print(eBA_n)
#############solving##################
#AA = [[eCD_n],[eDB_n],[eBA_n]]
AA = np.column_stack((np.column_stack((eCD_n,eDB_n)),eAC_n))
print('AA=')
print(AA)
BB = np.multiply(L,-eBA_n)
print('BB=')
print(BB)
x = np.linalg.solve(AA,BB)
print('x=')
print(x)
PM = np.multiply(x[2][0],-eAC_n)+np.multiply(L/2.0,-eBA_n)
print('M=')
print(PM)
