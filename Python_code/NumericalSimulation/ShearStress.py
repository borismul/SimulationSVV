def ShearStress(shearFlow,tFront,tRear,tTop,tBottom):
    shearStress = np.dot(shearFlow.T,np.transpose([1/tFront,1/tRear,1/tTop,1/tBottom]))
    return shearStress
    
#test module
import numpy as np