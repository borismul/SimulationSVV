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

#unit test ###!!!INCORRECT!!!### ##Check this one##
#import numpy as np
#from ChordLength import ChordLength
#import matplotlib.pyplot as plt
#l1 = 1
#l2 = 1
#liftDist = 1
#cr = 2
#ct = 1
#lift = 0
#steps = 100.
#dz = (l1+l2)/(steps)
#
#liftarray = np.zeros(steps+1)
#x = np.linspace(0,l1+l2,num = steps+1, endpoint=True)
#
#for z in x[::-1]:
#    c=ChordLength(cr,ct,l1,l2,z)
#    lift = Lift(z,liftDist,l1,l2,cr,ct,c,lift,dz)
#    liftarray[1/dz*z] = lift
#    print 1/dz*z
#print liftarray,x
#plt.plot(x,liftarray)
#plt.show()


####!!!tests!!!#### #INCORRECT#
#from ChordLength import ChordLength
#l1 = 1
#l2 = 1.
#z = [0,l1,l1+l2/2.,l1+l2]
#liftDist = 1
#cr = 2
#ct = 1
#prevLift = 0.1
#dz = 1
#expectedOutput = [0.5,0.5,0.6,0.1+1/3.]
#'''
#The expected output at the first two crossections (inside the constant part of the wingbox where no lift is acting) should be half of the total lift
#The expected output at the other two points are 
#'''
#output = []
#for i in range(4):
#    c=ChordLength(cr,ct,l1,l2,z[i])
#    lift = Lift(z[i],liftDist,l1,l2,cr,ct,c,prevLift,dz)
#    output.append(lift)
#if output == expectedOutput:
#    unit = True
#else:
#    unit = False
#if unit == False: raise IOError('unit test Lift False'):
    
#from ChordLength import ChordLength
#import numpy as np
#l1 = 1
#l2 = 1.
#z = [2.,1.5,1.,0.5,0.]
#liftDist = 1
#cr = 2
#ct = 1
#lift = 0
#dz = 0.5
#expectedOutput = [1/6.,5/12.,0.5,0.5,0.5]
#'''
#The expected output at the last three crossections (inside the constant part of the wingbox where no lift is acting) should be half of the total lift
#The expected output at the other two points are 
#'''
#output = []
#for i in range(5):
#    c=ChordLength(cr,ct,l1,l2,z[i])
#    lift = Lift(z[i],liftDist,l1,l2,cr,ct,c,lift,dz)
#    output.append(lift)
#if all(output >  expectedOutput-np.multiply(0.05,output)) and all(output < expectedOutput+np.multiply(0.05,output)):
#    unit = True
#else:
#    unit = False
#if unit == False: raise IOError('unit test Lift False')