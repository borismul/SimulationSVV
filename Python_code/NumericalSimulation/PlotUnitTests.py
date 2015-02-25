def PlotUnitTests(stepsZ,l1,l2,IArray,liftArray,coordinates,normalStressArray,plt):
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
    
    
    # plotting normal stress in rear and front webs of the wingbox vs y coordinate
    for i in range(2):
        plt.plot(coordinates[i*2+1,:],normalStressArray[stepsZ-2,i,:])
    plt.xlabel('y (m) -->')
    plt.ylabel('sigma (Pa) -->')
    plt.figure()
    
    # plotting normal stress in top and bottom webs of the wingbox vs x coordinate
    for i in range(2,4):
        plt.plot(coordinates[i*2,:],normalStressArray[stepsZ-2,i,:])
    plt.xlabel('x (m) -->')
    plt.ylabel('sigma (Pa) -->')
    