'''
This program calculates the coordinates on the webs and spars at a cross section of the wing box at an arbitrary z

Input variables: chord, steps along the x and y axis over a web, centroid (x and y)
Output variables: coordinates on the webs and spars
Output format: [8*[stepsXY*float]]
'''
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
chord = 1
stepsXY = 3
centroid = [0.,0.]
output = XYCoordinates(chord,stepsXY,centroid)
expectedOutput = [[0.25, 0.25, 0.25], [-0.05, 0., 0.05], [-0.25, -0.25, -0.25], [-0.05, 0., 0.05], [-0.25, 0., 0.25], [0.05, 0.05, 0.05], [-0.25, 0., 0.25], [-0.05, -0.05, -0.05]]
if all(output == expectedOutput):
    unit = True
else: unit = False

if unit == False: raise IOError('unit test XYcoordinates False')
#for i in range(4):
#    print i
#    plt.plot(xy[2*i,:],xy[2*i+1,:])
