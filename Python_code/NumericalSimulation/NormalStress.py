def NormalStress(moment,I,c,stepSizeXY):
    from XYCoordinates import XYCoordinates
    import numpy as np

    coordinates = XYCoordinates(c,stepSizeXY)    
    for i in range(4):
        sigma = np.multiply((moment[1]*I[0]- moment[0]*I[1])/(I[2]*I[0]-I[1]*I[1]),coordinates(i)) + np.multiply((moment[0]*I[2] - moment[1]*I[2])/(I[2]*I[0]-I[1]*I[1]),coordinates[i+1])
    
    return sigma
    