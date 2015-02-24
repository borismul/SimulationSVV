import numpy as np

def Moment(shearForce,prevMoment,dz):

    diff = np.multiply(shearForce,dz)
    diff_reversed = diff[::-1]
    return (prevMoment + diff_reversed)

# Unit test
#prevMoment = [1,1]
#shearForce = [2,2]
#dz = 0.5
#print(Moment(shearForce,prevMoment,dz))