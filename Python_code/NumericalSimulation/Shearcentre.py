#Function to calculate the shear flow in a crossection. 
def Shearcentre(chordLength, I, tFront, tRear, tBottom, tTop, stepsXY):
    import numpy as np
    #Inertias are defined:
    I[0] = Ixx
    #Since the section is cut at symmetry it has to have an equal number of steps on top and bottom
    if stepsXY%2 == 0:
        steps = (stepsXY)/2
    elif stepsXY%2 != 0:
        steps = (stepsXY-1)/2
    #Defining start points
    qb = 0
    iqs0 = 0
    qblist = np.array([])
    dy = 0.1*chordLength/stepsXY
    dx = 0.5*chordLength/stepsXY
#The section is cut at the axis of symmetry, i.e. x= -0.25c y=0 wrt our reference system
#Also the qs0 is determined through integral/integral equation. It IS valid.
    #From cut to top panel
    for y in np.linspace(0,0.05*chordLength,steps):
        qb -= 1/Ixx * tRear*y*dy
        iqs0 -= qb*dy
    #From rear to front panel
    for x in np.linspace(0.,0.5*chordLength,stepsXY):
        qb -= 1/Ixx * tTop*(0.05*chordLength)*dx
        iqs0 -= qb*dx
        qblist.append(qb)
    #Halfway from the top to the bottom panel
    for y in np.linspace(0,0.05*chordLength,steps):
        qb -= 1/Ixx * tFront*(0.05*chordLength-y)*dy
        iqs0 -= qb*dy
        qblist.append(qb)
    #the other parts follow from symmetry.
    #qs0 is now divided by the other integral to yield qs0.
    qs0 = iqs0/(0.5*chordLength + 0.1*chordLength)
    #Now we take moments about the cut. Symmetry now comes into play
    #shearx, is the X-coordinate of the shear centre wrt the rear panel
    Q = 0
    for x in np.linspace(0.,0.5*chordLength,stepsXY):
        Q += 0
    shearx = 2*Q
