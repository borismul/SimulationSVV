def Lift(z,liftDist,l2,l1):

    h = float(liftDist)/float(l2)
    if(z<=l1 and z>=0): Lift = 0
    elif(z>l1 and z<=l1+l2): Lift = float((z-l1))/float(l2)*h
    else: raise IOError('z outside wing')
    return Lift
#unit test
print Lift(10.5,1,10,10)

