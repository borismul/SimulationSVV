def ShearFlow(chordLength, shearForce, shearCenter, I, stepsXY,centroid, tFront, tTop, tRear, tBottom,plot):
    from XYCoordinates import XYCoordinates 
    from NumInt import NumInt
    import numpy as np
    import matplotlib.pyplot as plt
    Ixx = I[0]
    Ixy = I[1]
    Iyy = I[2]
    Sy = shearForce[0]
    Sx = shearForce[1]
    #section is cut at x = 0.25c, y = 0c
    coordinates = XYCoordinates(chordLength,stepsXY,centroid)
    constx = -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy**2)
    consty = -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy**2)
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
    for i in range(1,len(coordinates[7,:])):
        qb = qbRear[-1] + consty * NumInt(coordinates[7,:],tBottom*coordinates[6,:],coordinates[7,0],coordinates[7,i]) + constx * NumInt(coordinates[7,:],tBottom*coordinates[7,:],coordinates[7,0],coordinates[7,i])
        qbBottom.append(qb)
    qbarray = np.zeros((4,len(qbFront)))
    qbarray[0,:] = qbFront
    qbarray[1,:] = qbTop
    qbarray[2,:] = qbRear
    qbarray[3,:] = qbBottom
    qs0 = 0
    for i in range(4):
        if i%2==0:
            qs0 += NumInt(coordinates[1,:],qbarray[i,:],coordinates[1,0],coordinates[1,-1])/(1.2*chordLength)
        else:
            qs0 += NumInt(coordinates[5,:],qbarray[i,:],coordinates[5,0],coordinates[5,-1])/(1.2*chordLength)
    qFront = qbFront+qs0
    qRear = qbRear+qs0
    qTop = qbTop+qs0
    qBottom = qbBottom+qs0
    qarray = np.zeros((4,len(qFront)))
    qarray[0,:] = qFront
    qarray[1,:] = qTop
    qarray[2,:] = qRear
    qarray[3,:] = qBottom
    #print qFront[0] - qBottom[-1]
    if plot == True:
        plt.subplot(221)
        plt.plot(coordinates[1,:],qFront)
        plt.subplot(222)
        plt.plot(coordinates[1,:],qTop)
        plt.subplot(223)
        plt.plot(coordinates[1,:],qRear)
        plt.subplot(224)
        plt.plot(coordinates[1,:],qBottom)
        plot = False
    
    return qarray
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
