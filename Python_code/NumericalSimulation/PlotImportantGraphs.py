def PlotImportantGraphs(stepsZ,l1,l2,shearForceArray,momentArray,normalStressArray,shearStressArray,plt):
    import numpy as np
    
    # plotting shearforce vs z coordinate
    plt.figure()
    shearForceLabels = ['Sx','Sy']
    for i in range(2):
        plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),shearForceArray[:,i],label = shearForceLabels[i])
    plt.title('Shearforce vs z coordinate')
    plt.xlabel('z (m) -->')
    plt.ylabel('shearforce (N) -->')
    plt.legend()
    plt.figure()

    # plotting internal moment vs z
    momentLabels = ['Mx','My']
    for i in range(2):
        plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),momentArray[:,i],label = momentLabels[i])
    plt.title('Moment vs z coordinate')
    plt.xlabel('z (m) -->')
    plt.ylabel('Moment (Nm) -->')
    plt.legend()
    plt.figure()    
    
    # Finding the maximum and minimum normalstresses along the wingspan in all four sides of the wingbox
    maximum = np.amax(normalStressArray, axis = 2)
    minimum = np.amin(normalStressArray, axis = 2)    
    
    # plotting maximal and minimal stress in all all four sides of the wingbox vs z coordinate
    normalStressTitles = ['Maximum and minimum normal stresses in front spar vs z coordinate','Maximum and minimum normal stresses in rear spar vs z coordinate','Maximum and minimum normal stresses in top spar vs z coordinate','Maximum and minimum normal stresses in bottom spar vs z coordinate']    
    for i in range(4):
        plt.subplot(221+i)
        plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),maximum[:,i],'b',label = 'maximum')
        plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),minimum[:,i],'r',label = 'minimum')
        plt.title(normalStressTitles[i])
        plt.xlabel('z (m) -->')
        plt.ylabel('Normal Stress (N/m^2) -->')
        if (i==3):
            plt.legend(loc = 2)
        else: plt.legend()

    maxshear = np.amax(shearStressArray, axis = 2)
    minshear = np.amin(shearStressArray, axis = 2)    
        
    maxShearStressTitles = ['Maximum shear stress in front web','Maximum shear stress in rear web','Maximum shear stress in top web','Maximum shear stress in bottom web']
    plt.figure()
    for i in range(4):
        plt.subplot(221+i)
        plt.plot(range(stepsZ),maxshear[:,i],"b")
        plt.plot(range(stepsZ),minshear[:,i],"r")
        plt.title(maxShearStressTitles[i])
        plt.xlabel('z coordinate (m) -->')
        plt.ylabel('maximum shear stress (N/m^2) -->')

