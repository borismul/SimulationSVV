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
    qbFront1 = []
    for y in np.arange(yneg,ypos,dy):
        qb += consty * tFront * y * dy + constx * tFront * x * dy
        qbFront.append(qb)
    #Top
    qbTop1 = [qbFront[-1]]
    for x in np.arange(xneg,xpos,dx):
        qb += consty * tFront * y * dx + constx * tFront * x * dx
        qbTop.append(qb)
    #Rear
    qbRear = [qbTop[-1]]
    for y in np.arange(ypos,yneg,dy):
        qb += consty * tFront * y * dy + constx * tFront * x * dy
        qbRear.append(qb)
    #Bottom
    qbBottom = [qbRear[-1]]
    for x in np.arange(xneg, xpos,dx):
        qb += consty * tFront * y * dx + constx * tFront * x * dx
        qbBottom.append(qb)
#Put all the values of qb in an array
    qbarray = np.zeros((4,len(qbFront)))
    qbarray[0,:] = qbFront1
    qbarray[1,:] = qbTop
    qbarray[2,:] = qbRear
    qbarray[3,:] = qbBottom
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
##    return qarray
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
##
###unit test
###from XYCoordinates import XYCoordinates
###import numpy as np
###from NumInt import NumInt
###from ChordLength import ChordLength
###import matplotlib.pyplot as plt
###cr = 2
###ct = 1
###l1 = 5
###l2 = 10
###d = 1
###shearForce = [15.,1.5]
###I = [1.,0.,1.]
###stepsXY = 100
###centroid = [0.,0.]
###tFront = 0.001
###tRear = 0.001
###tTop = 0.001
###tBottom = 0.001
###for z in np.arange(0,l1+l2+d,d):
###    chord = ChordLength(cr,ct,l1,l2,z)
###    shearflow = ShearFlow(chord, shearForce,0,I,stepsXY,centroid,tFront,tTop, tRear, tBottom,True)
