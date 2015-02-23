import numpy as np

def Moment(shearForce,prevMoment,dz):
    
    prevMoment = np.sum(np.multiply(shearForce,dz))
    return -(prevMoment - np.multiply(shearForce,dz))

# Unit test
#prevMoment = [1,1]
#shearForce = [2,2]
#dz = 0.5
#print(Moment(shearForce,prevMoment,dz))