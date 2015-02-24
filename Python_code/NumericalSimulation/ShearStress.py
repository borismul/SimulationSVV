def ShearStress(shearFlow,tFront,tRear,tTop,tBottom):
    shearStress = np.dot(shearFlow.T,[[1/tFront,1/tRear,1/tTop,1/tBottom],[1/tFront,1/tRear,1/tTop,1/tBottom],[1/tFront,1/tRear,1/tTop,1/tBottom],[1/tFront,1/tRear,1/tTop,1/tBottom]])
    return shearStress.T
    
#test module
import numpy as np