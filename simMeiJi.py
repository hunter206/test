import numpy as np
import scipy

YAW =30*np.pi/180
ROLL = 20*np.pi/180
PITCH = 40*np.pi/180

C = np.matrix([0,0,0])
M = np.matrix([3,10,-4])
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
lBA_n = Cbn*lBA_b
print(Cbn)
print(lBA_n)



