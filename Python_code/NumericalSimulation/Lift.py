'''
This program calculates the shearforce due to the Lift at an arbitrary point of z.

Input variables: local z, total lift, lengths of the constant and tapered parts of the wing, 
root chord, tip chord, local chord, previous lift, stepsize in z
Output variables: shearforce due to the lift
Output format: float
'''
def Lift(z,liftDist,l1,l2,cr,ct,c,lift,dz):
    #create a distributed load changing with chord
    Lambda = float(liftDist/2.)/float(l2*(cr+ct)/2.)
    #for the constant part of the wing the the lift is the total lift/2
    if(z<=l1 and z>=0): lift = liftDist/2.
    #for the tapered part of the wing (where the lift acts) the lift is dececreasing towards the tip
    elif(z>l1 and z<=l1+l2): lift += Lambda*c*dz
    #elif(z == l1+l2): Lift = 0
    return lift

#unit test
import numpy as np
from ChordLength import ChordLength
import matplotlib.pyplot as plt
l1 = 1
l2 = 1
liftDist = 1
cr = 2
ct = 1
lift = 0
dz = 0.1

lift = np.zeros(101)
x = np.linspace(0,2,num = 101, endpoint=True)
print x
for z in reversed(x):
    c=ChordLength(cr,ct,l1,l2,z)
    lift[50*z] = Lift(z,liftDist,l1,l2,cr,ct,c,lift[50*z-1],0.02)
plt.plot(x,lift)
plt.show()