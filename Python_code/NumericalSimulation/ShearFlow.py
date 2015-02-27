'''
This program calculates the Shear Stress in a cross section of the wing box at an arbitrary point of z.

Input variables: local chord, total shearforce, torque,Moment of Ineria, the axis system along the webs and spars of the wingbox wrt the centroid, thicknesses of the webs and spars
Output variables: Shear stress along each web and spar.
Output format: [[stepsXY*float],[stepsXY*float],[stepsXY*float],[stepsXY*float]]
'''
def ShearFlow(chordLength, shearForce, torque, I, coordinates, tFront, tTop, tRear, tBottom):
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
        qb += consty * NumInt(coordinates[1,:],tFront*chordLength*coordinates[1,:],coordinates[1,i-1],coordinates[1,i]) + constx * NumInt(coordinates[1,:],tFront*chordLength*coordinates[0,:],coordinates[1,i-1],coordinates[1,i])
        qbFront.append(qb)
    #Top
    qbTop = [qbFront[-1]]
    for i in range(1,len(coordinates[4,:])):
        qb += consty * NumInt(coordinates[4,:],tTop*chordLength*coordinates[5,:],coordinates[4,i-1],coordinates[4,i]) + constx * NumInt(coordinates[4,:],tTop*chordLength*coordinates[4,:],coordinates[4,i-1],coordinates[4,i])
        qbTop.append(qb)
    #Rear
    qbRear = [qbTop[-1]]
    for i in range(1,len(coordinates[3,:])):
        qb += consty * NumInt(coordinates[3,:],tRear*chordLength*coordinates[3,:],coordinates[3,i-1],coordinates[3,i]) + constx * NumInt(coordinates[3,:],tRear*chordLength*coordinates[2,:],coordinates[3,i-1],coordinates[3,i])
        qbRear.append(qb)
    #Bottom
    qbBottom = [qbRear[-1]]
    for i in range(1,len(coordinates[6,:])):
        qb += consty * NumInt(coordinates[6,:],tBottom*chordLength*coordinates[7,:],coordinates[6,i-1],coordinates[6,i]) + constx * NumInt(coordinates[6,:],tBottom*chordLength*coordinates[6,:],coordinates[6,i-1],coordinates[6,i])
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
from XYCoordinates import XYCoordinates
chordLength = 1.
shearForce = [1.,0.]
torque = 1.
I = [1.,0.,1.]
stepsXY = 10.
centroid = [0.,0.]
coordinates = XYCoordinates(chordLength,stepsXY,centroid)
tFront = 1/1000.
tRear = 1/1000.
tTop = 1/1000.
tBottom = 1/1000.
output = ShearFlow(chordLength, shearForce, torque, I, coordinates, tFront, tTop, tRear, tBottom)
if output[-1,-1] == output[0,0]:
    unit = True
else: unit = False
if unit == False: print'unit test ShearFlow False'

