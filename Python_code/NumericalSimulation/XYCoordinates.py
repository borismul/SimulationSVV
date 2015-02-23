import numpy as np
import matplotlib.pyplot as plt
def XYCoordinates(chord,stepsXY,centroid):
    xRange = np.linspace(-0.25*chord,0.25*chord,num=stepsXY, endpoint=True)-centroid[0]
    yRange = np.linspace(-0.05*chord,0.05*chord,num=stepsXY, endpoint=True)-centroid[1]
    returnArray = np.zeros((8,stepsXY))
    #Front
    returnArray[0,:] = np.multiply(np.ones(stepsXY),(chord*0.25))-centroid[0]
    returnArray[1,:] = yRange - centroid[1]
    #Rear
    returnArray[2,:] = -np.multiply(np.ones(stepsXY),(chord*0.25))-centroid[0]
    returnArray[3,:] = yRange - centroid[1]
    #Top
    returnArray[4,:] = xRange - centroid[0]
    returnArray[5,:] = np.multiply(np.ones(stepsXY),(chord*0.05))-centroid[1]
    #Bottom
    returnArray[6,:] = xRange -centroid[0]
    returnArray[7,:] = -np.multiply(np.ones(stepsXY),(chord*0.05))-centroid[1]
    
    return returnArray

#Unit Test
#xy = XYCoordinates(1.98,100.,[0.,0.])
#
#for i in range(4):
#    print i
#    plt.plot(xy[2*i,:],xy[2*i+1,:])
