'''
This program calculates the centroid of the wingbox at one spanwise location.

Input variables: thicknesses of the wingbox webs and spars, local chord
Output variables: x and y coordinates of the centroid as
Output format: [float,float]
'''
def Centroid(tFront,tRear,tTop,tBottom,c):
#check for unusually large thicknesses
    if(tFront >= 0.5 or tRear >= 0.5 or tTop >= 0.1 or tBottom >=0.1):
        raise IOError('thicknesses are too big')
#Calculate the y coordinate of the centroid of each side of the wingbox
    yTop = 0.05*c-0.5*tTop*c
    yBottom = -0.05*c+0.5*tBottom*c
    ySide = 0.
#put the values in an array
    y = [yTop,yBottom,ySide,ySide]
#Calculate the x coordinate of the centroid of each side of the wingbox
    xFront = -0.25*c+0.5*tFront*c
    xRear = 0.25*c-0.5*tRear*c
    xTopBottom = 0.
#put the values in an array
    x = [xTopBottom,xTopBottom,xFront,xRear]
#Calculate the Area of each side of the wingbox
    ATop = tTop*c*0.5*c
    ABottom = tBottom*c*0.5*c
    AFront = tFront*c*0.1*c
    ARear = tRear*c*0.1*c
#put the values in an array
    A = [ATop,ABottom,AFront,ARear]

    xNum = 0.
    xDen = 0.
    yNum = 0.
    yDen = 0.
#calculate sum(x*A) and sum(y*A) (for numerator) and sum(x) and sum(y) for the denominator
    for i in range(4):
        xNum += x[i]*A[i]
        yNum += y[i]*A[i]
        xDen += A[i]
        yDen += A[i]
#Calcluate the x and y location of the centroid
    if xDen == 0: xCentroid = 0.
    else: xCentroid = xNum/xDen
    if yDen == 0: yCentroid = 0.
    else: yCentroid = yNum/yDen
    centroid = [xCentroid,yCentroid]
    return centroid

#unit test
##Test for equal thicknesses on each side. centroid = middle = [0,0]
tFront = 0.001
tTop = 0.001
tRear = 0.001
tBottom = 0.001
c = 10
if Centroid(tFront,tRear,tTop,tBottom,c) == [0,0]:
    unit = True
else: unit = False
##Test for only one contribution of top spar. centroid = centroid of the top spar = [0,0.495]
tFront = 0.000
tTop = 0.001
tRear = 0.000
tBottom = 0.000
c = 10
if Centroid(tFront,tRear,tTop,tBottom,c) == [0,0.495]:
    unit = True
else: unit = False

if unit == False: IOError('unit test Centroid False')