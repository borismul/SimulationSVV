#Function to calculate the shear flow in a crossection. (section is cut at x = 0.25c, y = 0c)
def ShearFlow(chordLength, shearForce, torque, I, coordinates, tFront, tTop, tRear, tBottom, sweep):
#Import functions needed
    from NumInt import NumInt
    import numpy as np
#Extract Moments of Inertia
    Ixx = I[0]
    Ixy = I[1]
    Iyy = I[2]
#Extract Shear Forces and moments
    Sx = shearForce[0]
    Sy = shearForce[1]
#Define the constant for qb calculation
    constx = -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy**2)
    consty = -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy**2)
#create starting value
    qb = 0  
#Calculate the shear stresses qb
    #Front
    qbFront = [0]
    for i in range(1,len(coordinates[1,:])):
        qb += consty * NumInt(coordinates[1,:],tFront*coordinates[1,:],coordinates[1,i-1],coordinates[1,i]) + constx * NumInt(coordinates[1,:],tFront*coordinates[0,:],coordinates[1,i-1],coordinates[1,i])
        qbFront.append(qb)
    #Top
    qbTop = [qbFront[-1]]
    for i in range(1,len(coordinates[4,:])):
        qb += consty * NumInt(coordinates[4,:],tTop*coordinates[5,:],coordinates[4,i-1],coordinates[4,i]) + constx * NumInt(coordinates[4,:],tTop*coordinates[4,:],coordinates[4,i-1],coordinates[4,i])
        qbTop.append(qb)
    #Rear
    qbRear = [qbTop[-1]]
    for i in range(1,len(coordinates[3,:])):
        qb += consty * NumInt(coordinates[3,:],tRear*coordinates[3,:],coordinates[3,i-1],coordinates[3,i]) + constx * NumInt(coordinates[3,:],tRear*coordinates[2,:],coordinates[3,i-1],coordinates[3,i])
        qbRear.append(qb)
    #Bottom
    qbBottom = [qbRear[-1]]
    for i in range(1,len(coordinates[6,:])):
        qb += consty * NumInt(coordinates[6,:],tBottom*coordinates[7,:],coordinates[6,i-1],coordinates[6,i]) + constx * NumInt(coordinates[6,:],tBottom*coordinates[6,:],coordinates[6,i-1],coordinates[6,i])
        qbBottom.append(qb)

#Put all the values of qb in an array
    qbarray = np.zeros((4,len(qbFront)))
    qbarray[0,:] = qbFront
    qbarray[1,:] = qbTop
    qbarray[2,:] = qbRear
    qbarray[3,:] = qbBottom
#Calculate qs0
    #Set an initial value for integration
    qbint = 0
    #Calculate int(p*qb)ds
    for i in range(4):
        if i%2==0:
            qbint += NumInt(coordinates[1,:],coordinates[i,:]*qbarray[i,:],coordinates[1,0],coordinates[1,-1])
        else:
            qbint += NumInt(coordinates[4,:],coordinates[i+3,:]*qbarray[i,:],coordinates[4,0],coordinates[4,-1])
    A = (coordinates[0,0]-coordinates[2,0])*(coordinates[5,0]-coordinates[7,0])
    qs0 = (torque - qbint)/(2*A)
    qFront = qbFront+qs0
    qRear = qbRear+qs0
    qTop = qbTop+qs0
    qBottom = qbBottom+qs0
    qarray = np.zeros((4,len(qFront)))
    qarray[0,:] = qFront
    qarray[2,:] = qTop
    qarray[1,:] = qRear
    qarray[3,:] = qBottom
    
    return qarray

#unit test
#from XYCoordinates import XYCoordinates
#import numpy as np
#from NumInt import NumInt
#from ChordLength import ChordLength
#import matplotlib.pyplot as plt
#cr = 2
#ct = 1
#l1 = 5
#l2 = 10
#d = 1
#shearForce = [15.,1.5]
#I = [1.,0.,1.]
#stepsXY = 100
#centroid = [0.,0.]
#tFront = 0.001
#tRear = 0.001
#tTop = 0.001
#tBottom = 0.001
#for z in np.arange(0,l1+l2+d,d):
#    chord = ChordLength(cr,ct,l1,l2,z)
#    shearflow = ShearFlow(chord, shearForce,0,I,stepsXY,centroid,tFront,tTop, tRear, tBottom,True)
import math as m
from XYCoordinates import XYCoordinates
chordLength = 1.
shearForce = [1.,0.]
torque = 1.
I = [1.,0.,1.]
stepsXY = 10.
centroid = [0.,0.]
coordinates = XYCoordinates(chordLength,stepsXY,centroid)
tFront = 0.0001
tRear = 0.0001
tTop = 0.0001
tBottom = 0.0001
plot = True
sweep = 180/m.pi
