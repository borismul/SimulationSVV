#Function to calculate the shear flow in a crossection. (section is cut at x = 0.25c, y = 0c)
def ShearFlow(chord, S, T, I, coordinates, tFront, tTop, tRear, tBottom, plot, sweep):
#Import functions needed
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
#Extract Moments of Inertia
    Ixx = I[0]
    Ixy = I[1]
    Iyy = I[2]
#Extract Shear Forces and moments
    Sx = S[0]
    Sy = S[1]
#Define the constant for qb calculation
    constx = -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy**2)
    consty = -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy**2)
#create starting value
    qb = 0
#The coordinates
    xpos = coordinates[0,0]
    xneg = coordinates[2,0]
    ypos = coordinates[5,0]
    yneg = coordinates[7,0]
    dx = coordinates[4,1]- coordinates[4,0]
    dy = coordinates[1,1]- coordinates[1,0]
#Calculate the shear stresses qb
    #Front
    qbFront = []
    for y in np.arange(yneg,ypos,dy):
        qb += consty * tFront * y * dy + constx * tFront * xpos * dy
        qbFront.append(qb)
    #Top
    qbTop = [qbFront[-1]]
    for x in np.arange(xpos,xneg,dx):
        qb += consty * tFront * ypos * dx + constx * tFront * x * dx
        qbTop.append(qb)
    #Rear
    qbRear = [qbTop[-1]]
    for y in np.arange(ypos,yneg,dy):
        qb += consty * tFront * y * dy + constx * tFront * xneg * dy
        qbRear.append(qb)
    #Bottom
    qbBottom = [qbRear[-1]]
    for x in np.arange(xneg, xpos,dx):
        qb += consty * tFront * yneg * dx + constx * tFront * x * dx
        qbBottom.append(qb)
    print len(qbBottom),len(qbFront)
#Put all the values of qb in an array
    qbarray = np.zeros((4,len(qbFront)))
    qbarray[0,:] = qbFront
    qbarray[1,:] = qbTop
    qbarray[2,:] = qbRear
    qbarray[3,:] = qbBottom
    print qbarray
###Calculate qs0
##    #Set an initial value for integration
##    qbint = 0
##    #Calculate int(p*qb)ds
##    for i in range(4):
##        if i%2==0:
##            qbint += NumInt(coordinates[1,:],coordinates[i,:]*qbarray[i,:],coordinates[1,0],coordinates[1,-1])
##        else:
##            qbint += NumInt(coordinates[4,:],coordinates[i+3,:]*qbarray[i,:],coordinates[4,0],coordinates[4,-1])
##    A = (coordinates[0,0]-coordinates[2,0])*(coordinates[5,0]-coordinates[7,0])
##    qs0 = (T - qbint)/(2*A)
##    qFront = qbFront+qs0
##    qRear = qbRear+qs0
##    qTop = qbTop+qs0
##    qBottom = qbBottom+qs0
##    qarray = np.zeros((4,len(qFront)))
##    qarray[0,:] = qFront
##    qarray[2,:] = qTop
##    qarray[1,:] = qRear
##    qarray[3,:] = qBottom
##    
    return qbarray
###    for y in coordinates[:,1]:
###        qb +=  * tFront*y*dy  * tFront*y*dy
###        List.append(qb)
###    for y in coordinates[:,3]:
###        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tRear*y*dy -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tRear*coordinates[0,2]*dx
###        List.append(qb)
###    for x in coordinates[:,4]:
###        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*coordinates[0,4]*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
###        List.append(qb)
###    for x in coordinates[:,4]:
###        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tBottom*coordinates[0,6]*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
###        List.append(qb)
#unit test
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
print ShearFlow(chordLength, shearForce, torque, I, coordinates, tFront, tTop, tRear, tBottom,plot, sweep)
