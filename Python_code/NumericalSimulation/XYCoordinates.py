
def XYCoordinates(chord,stepsXY,centroid):
    import numpy as np
    stepSizeX = (chord*0.5)/stepsXY
    stepSizeY = (chord*0.1)/stepsXY
    xRange = np.arange(0.,float(chord)*0.5,stepSizeX)-centroid[0]
    yRange = np.arange(0.,float(chord)*0.1,stepSizeY)-centroid[1]
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
print(XYCoordinates(3.,50.,[0.8,0.3]))