#plot the validation data and calculated data in one graph
def ValidationData(normalStress,shearStress,l1,l2,stepsZ,stepsXY):
    
    from ReadValidationData import ReadValidationData
    import matplotlib.pyplot as plt
    import numpy as np
    from StressANA import vonMisesFront
    from StressANA import vonMisesTop
    
    anaDataFrontX, anaDataFrontY = vonMisesFront()    
    anaDataTopX, anaDataTopY = vonMisesTop()    
    
    plt.figure()    
    
    valDataFront1 = ReadValidationData('front',1)
    valDataTop1 = ReadValidationData('top',1)
    
    valDataFront2 = ReadValidationData('front',2)
    valDataTop2 = ReadValidationData('top',2)
    
    valDataFront = np.multiply(valDataFront1 + valDataFront2,1/2.)
    valDataTop = np.multiply(valDataTop1 + valDataTop2,1/2.)

    plt.plot(valDataFront[:,1],valDataFront[:,4],label = 'Front average')
    plt.plot(valDataTop[:,1],valDataTop[:,4],label = 'Top average')
    
#    plt.plot(anaDataFrontX,anaDataFrontY,label = 'Front analytical calculation')
#    plt.plot(anaDataTopX,anaDataTopY,label = 'Top analytical calculation')

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
