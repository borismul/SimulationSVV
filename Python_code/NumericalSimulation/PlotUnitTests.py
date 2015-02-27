def PlotUnitTests(stepsZ,l1,l2,IArray,liftArray,coordinates,normalStressArray,shearStressArray,torque,ys,plt):
    import numpy as np
    
    # plotting moment of inertia vs z coordinate
    plt.figure()
    IplotLabels = ['Ixx','Ixy','Iyy']
    for i in range(3):
        plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),IArray[:,i], label = IplotLabels[i])
    
    plt.title('Moment of inertia vs z coordinate')
    plt.xlabel('z (m) -->')
    plt.ylabel('I (m^4) -->')
    plt.axis([0,l1+l2,-0.001,np.max(IArray)+0.001])
    plt.legend()
    plt.figure()   
    
    # plotting lift vs z coordinate
    plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),liftArray)
    plt.title('Lift vs z coordinate')
    plt.xlabel('z (m) -->')
    plt.ylabel('Lift (N) -->')
    plt.figure()
    
    normalStressTitles = ['Normal stress front and rear web vs z coordinate','Normal stress top and bottom web vs z coordinate']
    normalStressLabels = ['Normal stress front web','Normal stress rear web','Normal stress top web','Normal stress bottom web']
    # plotting normal stress in rear and front webs of the wingbox vs y coordinate
    for i in range(2):
        plt.plot(coordinates[i*2+1,:],normalStressArray[stepsZ-2,i,:],label = normalStressLabels[i])
    plt.title(normalStressTitles[0])
    plt.xlabel('y (m) -->')
    plt.ylabel('sigma (Pa) -->')
    plt.legend(loc = 5)
    plt.figure()
    
    # plotting normal stress in top and bottom webs of the wingbox vs x coordinate
    for i in range(2,4):
        plt.plot(coordinates[i*2,:],normalStressArray[stepsZ-2,i,:],label = normalStressLabels[i])
    plt.title(normalStressTitles[1])
    plt.xlabel('x (m) -->')
    plt.ylabel('sigma (Pa) -->')
    plt.legend(loc = 5)
    
    # plotting torque vs z coordinate
    plt.figure()
    plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),torque)
    plt.title('Torque vs z coordinate')
    plt.xlabel('z (m) -->')
    plt.ylabel('Torque (Nm) -->')

    # plotting shearstresses in root chord along x and y
    plt.figure()
    shearStressTitles = ['shear stress at root chord vs y location in front web','shear stress at root chord vs y location in rear web','shear stress at root chord vs x location in top web','shear stress at root chord vs x location in bottom web']
    for i in range(2):
        plt.subplot(221+i)
        plt.plot(coordinates[1,:],shearStressArray[0,i,:])
        plt.title(shearStressTitles[i])
        plt.xlabel('y location (m) -->')
        plt.ylabel('shear stress (N/m^2) -->')
            
    for i in range(2,4):
        plt.subplot(221+i)
        plt.plot(coordinates[4,:],shearStressArray[0,i,:])
        plt.title(shearStressTitles[i])
        plt.xlabel('x location (m) -->')
        plt.ylabel('shear stress (N/m^2) -->')