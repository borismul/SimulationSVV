def MomentOfInertia(tFront,tRear,tTop,tBottom,chord,centroid):    
    import numpy as np    
    
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
    y = y - centroid[1]
    
    #Calculate the x coordinate of the centroid of each side of the wingbox
    xFront = -0.25*chord+0.5*tFront*chord
    xRear = 0.25*chord-0.5*tRear*chord
    xTopBottom = 0.
    
    #put the values in an array
    x = np.array([xFront,xRear,xTopBottom,xTopBottom])
    x -= centroid[0]
    
    Ixx = 0.
    Ixy = 0
    Iyy = 0.
    
    for i in range(4):
        Ixx += (1./12.)*dimensions[i,0]*dimensions[i,1]*dimensions[i,1]*dimensions[i,1] + (y[i])*(y[i])*dimensions[i,0]*dimensions[i,1]
        Ixy += 0
        Iyy += (1./12.)*dimensions[i,1]*dimensions[i,0]*dimensions[i,0]*dimensions[i,0] + (x[i])*(x[i])*dimensions[i,0]*dimensions[i,1]

    return [Ixx,Ixy,Iyy]