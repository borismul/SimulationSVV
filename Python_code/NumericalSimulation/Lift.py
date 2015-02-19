def Lift(z,liftDist,l2,l1):
    import numpy as np
    h = liftDist/l2
    if z<l1 and z>0: Lift = 0
    if z>l1 and z<l1+l2: Lift = (z-l1)/l2*h
    else: raise IOError('z outside wing')
    return Lift
#unit test
print Lift(0,1,1,1)
