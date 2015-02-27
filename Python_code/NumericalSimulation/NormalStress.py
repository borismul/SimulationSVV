'''
This program calculates the Normal Stress in a cross section of the wing box at an arbitrary point of z.

Input variables: moments acting on the wing, Moment of Ineria, local chord, the axis system along the webs and spars of the wingbox wrt the centroid
Output variables: Normal stress along each web and spar.
Output format: [[stepsXY*float],[stepsXY*float],[stepsXY*float],[stepsXY*float]]
'''
def NormalStress(moment,I,c,coordinates):
    import numpy as np
    #make an empty array for the data
    sigma = np.zeros((4,len(coordinates[0,:])))
    for i in range(4):
        #calculating the normal stress through matrix multiplication
        sigma[i,:] = np.multiply((moment[1]*I[0]- moment[0]*I[1])/(I[2]*I[0]-I[1]*I[1]),coordinates[2*i,:]) + np.multiply((moment[0]*I[2] - moment[1]*I[2])/(I[2]*I[0]-I[1]*I[1]),coordinates[2*i+1,:])
    return sigma
    
#unit test
#import numpy as np
#from XYCoordinates import XYCoordinates
#c = 1.
#stepsXY = 10.
#centroid = [0.,0.]
#coordinates = XYCoordinates(c,stepsXY,centroid)
#moment = [1.,0.]
#I = [1.,0.,1.]
#output =  NormalStress(moment,I,c,coordinates)
#expectedOutput = np.zeros((4,stepsXY))
#for i in range(4):
#    expectedOutput[i,:] = coordinates[2*i+1,:]
#if all(abs(output) >=  abs(expectedOutput-np.multiply(0.05,output))) and all(abs(output) <= abs(expectedOutput+np.multiply(0.05,output))):
#    unit = True
#else: unit = False
#if unit == False: raise IOError('unit test MomentOfInertia False')