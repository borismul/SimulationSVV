def Lift(z,liftDist,l2,l1):
    import numpy as np
    h = liftDist/l2
    if z<l1: Lift = 0
    if z>l1 and z<l1+l2: Lift = (z-l1)/l2*h
    else: raise IOError('thicknesses are too big')
return Lift
#unit test
#    Lift(1,)