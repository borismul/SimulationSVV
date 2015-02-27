def PlotVerificationData(normalStressArray,shearStressArray,stepsXY):
    import matplotlib.pyplot as plt
    
    plt.figure()
    plt.subplot(121)
    plt.plot(range(len(normalStressArray[:,2,int(stepsXY/2.)])),normalStressArray[:,2,int(stepsXY/2.)])
    plt.subplot(122)
    plt.plot(range(len(normalStressArray[:,0,int(stepsXY/2.)])),normalStressArray[:,0,int(stepsXY/2.)])
    
    plt.figure()
    plt.subplot(121)
    plt.plot(range(len(shearStressArray[:,2,int(stepsXY/2.)])),shearStressArray[:,2,int(stepsXY/2.)])
    plt.subplot(122)
    plt.plot(range(len(shearStressArray[:,0,int(stepsXY/2.)])),shearStressArray[:,0,int(stepsXY/2.)])