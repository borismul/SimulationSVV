def ValidationData(normalStress,shearStress,l1,l2,stepsZ,stepsXY):
    
    from ReadValidationData import ReadValidationData
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure()    
    
    valDataFront1 = ReadValidationData('front',1)
    valDataTop1 = ReadValidationData('top',1)
    
    valDataFront2 = ReadValidationData('front',2)
    valDataTop2 = ReadValidationData('top',2)
    
    plt.plot(valDataFront1[:,1],valDataFront1[:,4],label = 'Front inside')
    plt.plot(valDataFront2[:,1],valDataFront2[:,4],label = 'Front outside')
    plt.plot(valDataTop1[:,1],valDataTop1[:,4],label = 'Top inside')
    plt.plot(valDataTop2[:,1],valDataTop2[:,4],label = 'Top outside')

    plt.title('Von Mises Stress vs z')
    plt.xlabel('z(m) -->')
    plt.ylabel('Von Mises Stress (N/m^2) -->')

    frontNormalStress = normalStress[:,0,int(stepsXY/2.)]
    frontShearStress = shearStress[:,0,int(stepsXY/2.)]
    topNormalStress = normalStress[:,2,int(stepsXY/2.)]
    topShearStress = shearStress[:,2,int(stepsXY/2.)]
    
    vonMissesFront = np.sqrt(np.square(frontNormalStress) + 3*np.square(frontShearStress))
    vonMissesTop = np.sqrt(np.square(topNormalStress) + 3*np.square(topShearStress))
    
    plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),vonMissesFront,label = 'Front numerical calculation')
    plt.plot(np.multiply(range(stepsZ),(l1+l2)/stepsZ),vonMissesTop,label = 'Top numerical calculation')
    plt.legend()
