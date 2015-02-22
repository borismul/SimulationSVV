def ShearFlow(chordLength, shearForce, shearCenter, I, stepsXY,centroid, tFront, tTop, tRear, tBottom):
    Ixx = I[0]
    Ixy = I[1]
    Iyy = I[2]
    Sy = shearForce[0]
    Sx = shearForce[1]
    #section is cut at x = 0.25c, y = 0c  
    print chordLength,stepsXY,centroid
    coordinates = XYCoordinates(chordLength,stepsXY,centroid)
    dx = 0.5*chordLength/stepsXY
    dy = 0.1*chordLength/stepsXY
    constx = -100#-(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy**2)
    consty = -100#-(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy**2)
    #Front
    qbFront = [0]
    for i in range(1,len(coordinates[1,:])):
        qb = consty * NumInt(coordinates[1,:],tFront*coordinates[1,:],coordinates[1,0],coordinates[1,i]) + constx * NumInt(coordinates[1,:],tFront*coordinates[0,:],coordinates[1,0],coordinates[1,i])
        qbFront.append(qb)
    #Top
    qbTop = [qbFront[-1]]
    for i in range(1,len(coordinates[5,:])):
        qb = qbFront[-1] + consty * NumInt(coordinates[5,:],tTop*coordinates[4,:],coordinates[5,0],coordinates[5,i]) + constx * NumInt(coordinates[5,:],tTop*coordinates[5,:],coordinates[5,0],coordinates[5,i])
        qbTop.append(qb)
    #Rear
    qbRear = [qbTop[-1]]
    for i in range(1,len(coordinates[3,:])):
        qb = qbTop[-1] + consty * NumInt(coordinates[3,:],tRear*coordinates[3,:],coordinates[3,0],coordinates[3,i]) + constx * NumInt(coordinates[3,:],tRear*coordinates[2,:],coordinates[3,0],coordinates[3,i])
        qbRear.append(qb)
    #Bottom
    qbBottom = [qbRear[-1]]
    for i in range(1,len(coordinates[6,:])):
        qb = qbRear[-1] + consty * NumInt(coordinates[7,:],tBottom*coordinates[6,:],coordinates[7,0],coordinates[7,i]) + constx * NumInt(coordinates[7,:],tBottom*coordinates[7,:],coordinates[7,0],coordinates[7,i])
        qbBottom.append(qb)
    plt.subplot(221)
    plt.plot(coordinates[1,:],qbFront)
    plt.subplot(222)
    plt.plot(coordinates[1,:],qbTop)
    plt.subplot(223)
    plt.plot(coordinates[1,:],qbRear)
    plt.subplot(224)
    plt.plot(coordinates[1,:],qbBottom)

    
    return qb
#    for y in coordinates[:,1]:
#        qb +=  * tFront*y*dy  * tFront*y*dy
#        List.append(qb)
#    for y in coordinates[:,3]:
#        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tRear*y*dy -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tRear*coordinates[0,2]*dx
#        List.append(qb)
#    for x in coordinates[:,4]:
#        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*coordinates[0,4]*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
#        List.append(qb)
#    for x in coordinates[:,4]:
#        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tBottom*coordinates[0,6]*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
#        List.append(qb)

#unit test
from XYCoordinates import XYCoordinates
import numpy as np
from NumInt import NumInt
from ChordLength import ChordLength
import matplotlib.pyplot as plt
cr = 2
ct = 1
l1 = 5
l2 = 10
d = 1
shearForce = [15.,1.5]
I = [1.,0.,1.]
stepsXY = 100
centroid = [0.,0.]
tFront = 0.001
tRear = 0.001
tTop = 0.001
tBottom = 0.001
for z in np.arange(0,l1+l2+d,d):
    chord = ChordLength(cr,ct,l1,l2,z)
    print z
    shearflow = ShearFlow(chord, shearForce,0,I,stepsXY,centroid,tFront,tTop, tRear, tBottom)
