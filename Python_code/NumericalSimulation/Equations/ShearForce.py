def ShearForce(lift, engineWeight, T, fuelliters, fueldensity, l1, l2, l3, z, g):
    if (z >= 0 and z <= l1):
        fuelmass = (l1 - z)/l1 * fuelliters * fueldensity * g
        S_y = lift - engineWeight - fuelmass
        S_x =  T
    elif (z >= l1 and z <= l3):
        S_y = lift - engineWeight
        S_x =  T
    elif (z >= l3 and z <= (l1+l2)):
        S_y = lift
        S_x = 0
    return S_y, S_x
