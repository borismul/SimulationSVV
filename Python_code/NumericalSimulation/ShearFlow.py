#Function to calculate the shear flow in a crossection. (section is cut at x = 0.25c, y = 0c)
def ShearFlow(chordLength, shearForce, Moment, shearCenter, I, coordinates, tFront, tTop, tRear, tBottom,plot):
#Import functions needed
    from NumInt import NumInt
    import numpy as np
    import matplotlib.pyplot as plt
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
#calculate qs0
    w = moment[0]/    
    qs0 = 0
    for i in range(4):
        if i%2==0:
            qs0 += NumInt(coordinates[1,:],qbarray[i,:],coordinates[1,0],coordinates[1,-1])/(1.2*chordLength)
        else:
            qs0 += NumInt(coordinates[4,:],qbarray[i,:],coordinates[4,0],coordinates[4,-1])/(1.2*chordLength)
    qFront = qbFront+qs0
    qRear = qbRear+qs0
    qTop = qbTop+qs0
    qBottom = qbBottom+qs0
    qarray = np.zeros((4,len(qFront)))
    qarray[0,:] = qFront
    qarray[1,:] = qTop
    qarray[2,:] = qRear
    qarray[3,:] = qBottom
    label = str(chordLength)
    if plot == True:
        plt.figure()
        plt.subplot(221)
        plt.plot(coordinates[1,:],qFront, label = label)
        plt.subplot(222)
        plt.plot(coordinates[4,:],qTop, label = label)
        plt.subplot(223)
        plt.plot(coordinates[1,:],qRear, label = label)
        plt.subplot(224)
        plt.plot(coordinates[4,:],qBottom, label = label) ##Last picture does weird!?!
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0.)
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
