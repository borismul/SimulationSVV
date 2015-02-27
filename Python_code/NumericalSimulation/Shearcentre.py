#Function to calculate the shear flow in a crossection. 
def Shearcentre(chordLength, I, tFront, tRear, tBottom, tTop, stepsXY):
    #Inertias are defined:
    Ixx = I[0]
    #Since the section is cut at symmetry it has to have an equal number of steps on top and bottom
    if stepsXY%2 == 0:
        steps = (stepsXY)/2
    elif stepsXY%2 != 0:
        steps = (stepsXY-1)/2
    #Defining start points
    qb = 0
    iqs0 = 0
    qblist = []
    dy = 0.1*chordLength/stepsXY
    dx = 0.5*chordLength/stepsXY
#The section is cut at the axis of symmetry, i.e. x= -0.25c y=0 wrt our reference system
#Also the qs0 is determined through integral/integral equation. It IS valid.
    #From cut to top panel
    for y in np.linspace(0,0.05*chordLength,steps):
        qb -= 1/Ixx * tRear*y*dy
        iqs0 += qb/tRear*dy
    #From rear to front panel
    for x in np.linspace(0.,0.5*chordLength,stepsXY):
        qb -= 1/Ixx * tTop*(0.05*chordLength)*dx
        iqs0 += qb/tTop*dx
        qblist.append(qb)
        list1=len(qblist)
    #Halfway from the top to the bottom panel
    for y in np.linspace(0,0.05*chordLength,steps):
        qb -= 1/Ixx * tFront*(0.05*chordLength-y)*dy
        iqs0 += qb/tFront*dy
        qblist.append(qb)
        list2=len(qblist)
    #the other parts follow from symmetry.
    #qs0 is now divided by the other integral to yield qs0.
    qs0 = -iqs0/(0.5*chordLength/tTop + 0.05*chordLength/tFront+0.05*chordLength/tRear)
    #Now we take moments about the cut. Symmetry now comes into play
    #shearx, is the X-coordinate of the shear centre wrt the rear panel
    Qx = 0
    for x in np.linspace(0.,0.5*chordLength,stepsXY):
        Qx += (qs0+qblist[0,list1-1])*0.05*chordLength*dx
    for y in np.linspace(0,0.05*chordLength,steps):
        Qx += (qs0+qblist[list1-1, list2-1])*0.5*chordLength*dy
    shearx = 2*Qx
    return shearx

import numpy as np
print(Shearcentre(5, [1,0,0], 1, 1, 1, 1, 5))
