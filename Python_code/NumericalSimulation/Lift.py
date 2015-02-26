'''
This program calculates the shearforce due to the Lift at an arbitrary point of z.

Input variables: local z, total lift, lengths of the constant and tapered parts of the wing, 
root chord, tip chord, local chord, previous lift, stepsize in z
Output variables: shearforce due to the lift
Output format: float
'''
def Lift(z,liftDist,l1,l2,cr,ct,c,lift,dz):
    #create a distributed load changing with chord
    Lambda = float(liftDist/2.)/float(l2*(cr+ct)/2.) #1/3
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
steps = 100.
dz = (l1+l2)/(steps)

liftarray = np.ones(steps+1)
x = np.linspace(0,l1+l2,num = steps+1, endpoint=True)
plt.close()
i=len(x)-1
for z in x[::-1]:
    c=ChordLength(cr,ct,l1,l2,z)
    lift = Lift(z,liftDist,l1,l2,cr,ct,c,lift,dz)
    liftarray[i] = lift
    #print z
    i -= 1
#print liftarray,x
plt.plot(x,liftarray)
plt.show()

#if all(liftarray >  expectedOutput-np.multiply(0.05,output)) and all(output < expectedOutput+np.multiply(0.05,output)):
#    unit = True
#else:
#    unit = False
#if unit == False: raise IOError('unit test Lift False')

'''
As can be seen in the plotted figure, the lift distribution is as expected.
The graph decreases quadratic from 0.5 to 0.

'''