def ShearFlow(chordLength, shearForce, shearCenter, I, stepsXY,centroid, tFront, tTop, tRear, tBottom):
    Ixx = I[0]
    Iyy = I[1]
    Ixy = I[2]
    Sy = shearForce[0]
    Sx = shearForce[1]
    #section is cut at x = 0.25c, y = 0c   
    coordinates = XYCoordinates(chordLength,stepsXY,centroid)
    dx = 0.5*chordLength/stepsXY
    dy = 0.1*chordLength/stepsXY
    qb = 0.
    List = []
    for y in coordinates[:,1]:
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tFront*y*dy -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tFront*coordinates[0,0]*dx
        List.append(qb)
    for y in coordinates[:,3]:
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tRear*y*dy -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tRear*coordinates[0,2]*dx
        List.append(qb)
    for x in coordinates[:,4]:
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*coordinates[0,4]*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
        List.append(qb)
    for x in coordinates[:,4]:
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tBottom*coordinates[0,6]*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
        List.append(qb)

#unit test
from XYCoordinates import XYCoordinates
import numpy as np