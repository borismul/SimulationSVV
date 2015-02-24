def ShearForce(lift, engineWeight, T, l1, l2, l3, z, fuelWeight):
#These are all SI units
    if (z >= 0 and z <= l1):
        # in this length all the shear forces act
        S_y = lift + engineWeight - fuelWeight
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
