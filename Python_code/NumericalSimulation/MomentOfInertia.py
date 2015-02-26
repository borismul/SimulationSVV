'''
This program calculates the Moment of Inertia of a cross section of the wing box at an arbitrary point of z.

Input variables: thicknesses of the wingbox spars and webs, local chord, centroid (x and y)
Output variables: moment of inertia (Ixx,Ixy,Iyy)
Output format: [float,float,float]
'''
def MomentOfInertia(tFront,tRear,tTop,tBottom,chord,centroid):
#make an array with the dimentions of the wingbox (thickness(4x),length(4x))         
    dimensions = np.zeros((4,2))
    dimensions[0,0] = tFront*chord
    dimensions[0,1] = chord*0.1
    dimensions[1,0] = tRear*chord
    dimensions[1,1] = chord*0.1
    dimensions[2,0] = chord*0.5
    dimensions[2,1] = tTop*chord
    dimensions[3,0] = chord*0.5
    dimensions[3,1] = tBottom * chord
    
    #Calculate the y coordinate of the centroid of each side of the wingbox
    yTop = 0.05*chord-0.5*tTop*chord
    yBottom = -0.05*chord+0.5*tBottom*chord
    ySide = 0.
    
    #put the values in an array
    y = np.array([ySide,ySide,yTop,yBottom])
    #convert to centroid-centered coordinate system
    y = y - centroid[1]
    
    #Calculate the x coordinate of the centroid of each side of the wingbox
    xFront = -0.25*chord+0.5*tFront*chord
    xRear = 0.25*chord-0.5*tRear*chord
    xTopBottom = 0.
    
    #put the values in an array
    x = np.array([xFront,xRear,xTopBottom,xTopBottom])
    #convert to centroid-centered coordinate system
    x -= centroid[0]
    
    Ixx = 0.
    Ixy = 0
    Iyy = 0.
    #calculate the contributions of each web/spar (1/12*h*b^3+x^2*h*b) and adding them up
    for i in range(4):
        Ixx += (1./12.)*dimensions[i,0]*dimensions[i,1]**3 + (y[i])**2*dimensions[i,0]*dimensions[i,1]
        Ixy += x[i]*y[i]*dimensions[i,0]*dimensions[i,1]
        Iyy += (1./12.)*dimensions[i,1]*dimensions[i,0]**3 + (x[i])**2*dimensions[i,0]*dimensions[i,1]
    return [Ixx,Ixy,Iyy]
    
#unit test
import numpy as np   
tFront = 1/1000.
tRear = 1/1000.
tTop = 1/1000.
tBottom = 1/1000.
chord = 10
centroid = [0,0]
output = MomentOfInertia(tFront,tRear,tTop,tBottom,chord,centroid)
expectedOutput = [2/75.,0,1/3.]
if all(output >=  expectedOutput-np.multiply(0.05,output)) and all(output <= expectedOutput+np.multiply(0.05,output)):
    unit = True
else: unit = False
if unit == False: raise IOError('unit test MomentOfInertia False')