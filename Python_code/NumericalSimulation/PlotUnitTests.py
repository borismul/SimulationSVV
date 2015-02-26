def PlotUnitTests(stepsZ,l1,l2,IArray,liftArray,coordinates,normalStressArray,torque,plt):
    import numpy as np
    
    # plotting moment of inertia vs z coordinate
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