def PlotVerificationData(normalStressArray,shearStressArray,stepsXY,l1,l2):
    import matplotlib.pyplot as plt
    import numpy as np
    from StressANA import shearstress
    from StressANA import Normstress
    
    ilstTopShear, q01lst, anaTopShear, q23lst, q34lst, q45lst, q01lst = shearstress(0,0.05)
    ilstFrontShear, q01lst, iets, anaFrontShear, q34lst, q45lst, q01lst = shearstress(0.25,0)
    
    ilstTopNorm, anaTopNorm= Normstress(0,0.05)
    ilstFrontNorm, anaFrontNorm = Normstress(0.25,0)
    
    plt.figure()
    plt.subplot(121)
    plt.title('Top spar normal Stress')
    plt.xlabel('z location (m) -->')
    plt.ylabel('normal stress (N/m^2) -->')
    plt.plot(np.multiply(range(len(normalStressArray[:,2,int(stepsXY/2.)])),(l1+l2)/len(normalStressArray[:,2,int(stepsXY/2.)])),normalStressArray[:,2,int(stepsXY/2.)],label = 'Numerical')
    plt.plot(ilstTopNorm,anaTopNorm,label = 'Analytical')    
    plt.legend()
    
    plt.subplot(122)
    plt.plot(np.multiply(range(len(normalStressArray[:,0,int(stepsXY/2.)])),(l1+l2)/len(normalStressArray[:,0,int(stepsXY/2.)])),normalStressArray[:,0,int(stepsXY/2.)],label = 'Numerical')
    plt.plot(ilstFrontNorm,anaFrontNorm,label = 'Analytical')    
    plt.title('Front spar normal Stress')
    plt.xlabel('z location (m) -->')
    plt.ylabel('normal stress (N/m^2) -->')
    plt.legend()
    
    plt.figure()
    plt.subplot(121)
    plt.title('Top spar shear Stress')
    plt.xlabel('z location (m) -->')
    plt.ylabel('shear stress (N/m^2) -->')
    plt.plot(np.multiply(range(len(shearStressArray[:,2,int(stepsXY/2.)])),(l1+l2)/len(shearStressArray[:,2,int(stepsXY/2.)])),shearStressArray[:,2,int(stepsXY/2.)],label = 'Numerical')
    plt.plot(ilstTopShear,anaTopShear,label = 'Analytical')    
    plt.legend()
    
    plt.subplot(122)
    plt.title('Front spar shear Stress')
    plt.xlabel('z location (m) -->')
    plt.ylabel('shear stress (N/m^2) -->')
    plt.plot(np.multiply(range(len(shearStressArray[:,0,int(stepsXY/2.)])),(l1+l2)/len(shearStressArray[:,0,int(stepsXY/2.)])),shearStressArray[:,0,int(stepsXY/2.)],label = 'Numerical')
    plt.plot(ilstFrontShear,anaFrontShear,label = 'Analytical')
    plt.legend()
    
    plt.figure()
    plt.subplot(121)
    plt.title('Shear stress vs z')
    plt.xlabel('z location (m) -->')
    plt.ylabel('Shear stress (N/m^2)')
    plt.plot(ilstTopShear,anaTopShear,label = 'Top spar')
    plt.plot(ilstFrontShear,anaFrontShear,label = 'Front spar')
    plt.legend()
    plt.subplot(122)
    plt.title('Normal stress vs z')
    plt.xlabel('z location (m) -->')
    plt.ylabel('Normal stress (N/m^2)')
    plt.plot(ilstTopNorm,anaTopNorm,label = 'Top spar')
    plt.plot(ilstFrontNorm,anaFrontNorm,label = 'Front spar')
    plt.legend()