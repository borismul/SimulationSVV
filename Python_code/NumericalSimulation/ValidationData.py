def ValidationData():
    
    from ReadValidationData import ReadValidationData
    import matplotlib.pyplot as plt
    
    valDataFront1 = ReadValidationData('front',1)
    valDataTop1 = ReadValidationData('top',1)
    
    valDataFront2 = ReadValidationData('front',2)
    valDataTop2 = ReadValidationData('top',2)
    
    plt.plot(valDataFront1[:,1],valDataFront1[:,4],label = 'Front inside')
    plt.plot(valDataTop1[:,1],valDataTop1[:,4],label = 'Top outside')
    plt.plot(valDataFront2[:,1],valDataFront2[:,4],label = 'Front inside')
    plt.plot(valDataTop2[:,1],valDataTop2[:,4],label = 'Top inside')

    plt.title('Von Mises Stress vs z')
    plt.xlabel('z(m) -->')
    plt.ylabel('Von Mises Stress (N/m^2) -->')
    plt.legend()
    