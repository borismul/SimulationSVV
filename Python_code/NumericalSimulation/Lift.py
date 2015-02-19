def Lift(z,liftDist,l1,l2,cr,ct,c,Lift,dz):
    Lambda = float(liftDist/2.)/float(l2*(cr+ct)/2.)
    if(z<=l1 and z>=0): Lift = liftDist/2.
    elif(z>l1 and z<=l1+l2): Lift -= Lambda*c*dz
    else: raise IOError('z outside wing')
    return Lift

#unit test
#import numpy as np
#from ChordLength import ChordLength
#import matplotlib.pyplot as plt
#
#lift = np.zeros(201)
#for z in np.arange(0,20.1,0.1):
#    cr = 4.
#    ct = 1.
#    l1 = 5.
#    l2 = 15.
#    liftdist = 1.
#    c=ChordLength(cr,ct,l1,l2,z)
#    lift[10*z] = Lift(z,liftdist,l1,l2,cr,ct,c,lift[10*z-1],0.1)
#    x = np.arange(0,20.1,0.1)
#plt.plot(x,lift)
#plt.show()

