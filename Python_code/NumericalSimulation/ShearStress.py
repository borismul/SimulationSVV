'''
This program calculates the shearstress distribution on the cross section of the wing box at an arbitrary z

Input variables: shearflow distribution, thicknesses of the spars and webs
Output variables: shearstress distribution in each spar/web
Output format: [[stepsXY*float],[stepsXY*float],[stepsXY*float],[stepsXY*float]]
'''
def ShearStress(shearFlow,tFront,tRear,tTop,tBottom,c):
    #calculate shearflow/thickness as matrix operation
    import numpy as np
    shearStress = np.dot(shearFlow.T,[[1/c/tFront,0,0,0],[0,1/c/tRear,0,0],[0,0,1/c/tTop,0],[0,0,0,1/c/tBottom]])
    return shearStress
    
#test module
#import numpy as np
#stepsXY = 3
#shearFlow = np.ones((4,stepsXY))
#tFront = 1/1000.
#tRear = 1/2000.
#tTop = 1/3000.
#tBottom = 1/4000.
#c = 1
#output = ShearStress(shearFlow,tFront,tRear,tTop,tBottom,c)
#expectedOutput = [[1000,2000,3000,4000],[1000,2000,3000,4000],[1000,2000,3000,4000]]
#if all(output == expectedOutput):
#    unit = True
#else: unit = False
#
#if unit == False: raise IOError('unit test ShearStress False')