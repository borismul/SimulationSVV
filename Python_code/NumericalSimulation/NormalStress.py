def NormalStress(moment,I,c,stepsXY,centroid):
    from XYCoordinates import XYCoordinates
    import numpy as np

    coordinates = XYCoordinates(c,stepsXY,centroid)
    sigma = np.zeros((4,stepsXY))
    for i in range(4):
        sigma[i,:] = np.multiply((moment[1]*I[0]- moment[0]*I[1])/(I[2]*I[0]-I[1]*I[1]),coordinates[2*i,:]) + np.multiply((moment[0]*I[2] - moment[1]*I[2])/(I[2]*I[0]-I[1]*I[1]),coordinates[2*i+1,:])
    return sigma
    