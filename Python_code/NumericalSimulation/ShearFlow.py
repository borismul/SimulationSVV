def ShearFlow(chordLength, shearForce, shearCenter, I, stepsXY):
    Ixx = I[0]
    Iyy = I[1]
    Ixy = I[2]
    Sy = shearForce[0]
    Sx = ShearForce[1]
    #section is cut at x = 0.25c, y = 0c
    x = 0.25c
    y = 0.
    dy = 0.05*chordLength/
    qb = 0.
    List = []
    for y in np.arange(0,0.05*chordLength,dy):
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tFront*y*dy -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tFront*x*dy
        List.append([qb,x,y])
    for x in np.arange(0,0.05*chordLength,dx):
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*y*dx -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tTop*x*dx
        List.append([qb,x,y])
    for y in np.arange(0.05*chordLength,0.05*chordLength,dy):
        qb += -(Sx*Ixx - Sy*Ixy)/(Ixx*Iyy - Ixy^2) * tFront*y*dy -(Sy*Iyy - Sx*Ixy)/(Ixx*Iyy - Ixy^2) * tFront*x*dy
        List.append([qb,x,y])
