
def XYCoordinates(chord,stepsXY,centroid):
    import numpy as np
    xRange = np.linspace(-0.25*chord,0.25*chord,num=stepsXY, endpoint=True)-centroid[0]
    yRange = np.linspace(-0.05*chord,0.05*chord,num=stepsXY, endpoint=True)-centroid[1]
    returnArray = np.zeros((8,stepsXY))
    returnArray[0,:] = np.multiply(np.ones(stepsXY),(chord*0.25))-centroid[0]
    returnArray[1,:] = yRange
    returnArray[2,:] = -np.multiply(np.ones(stepsXY),(chord*0.25))-centroid[0]
    returnArray[3,:] = yRange
    returnArray[4,:] = np.multiply(np.ones(stepsXY),(chord*0.05))-centroid[1]
    returnArray[5,:] = xRange
    returnArray[6,:] = -np.multiply(np.ones(stepsXY),(chord*0.05))-centroid[1]
    returnArray[7,:] = xRange

    return returnArray

#Unit Test
XYCoordinates(1.98,100.,[0.,0.])
