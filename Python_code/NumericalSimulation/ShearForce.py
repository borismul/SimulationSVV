def ShearForce(lift, engineWeight, T, fuelliters, fueldensity, l1, l2, l3, z, g):
#These are all SI units
    if (z >= 0 and z <= l1):
        # in this length all the shear forces act
        fuelmass = (l1 - z)/l1 * fuelliters * fueldensity * g # (N)
        S_y = lift - engineWeight - fuelmass
        S_x =  T
    elif (z >= l1 and z <= l3):
        #Only the engine + lift
        S_y = lift - engineWeight
        S_x =  T
    elif (z >= l3 and z <= (l1+l2)):
        #Just the lift
        S_y = lift
        S_x = 0
    else: raise IOError('z outside wing')
    return S_x, S_y
#it returns a reference error if z is outside the range of the wingspan.
