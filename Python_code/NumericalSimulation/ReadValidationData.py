def ReadValidationData(spar,z):
    if (spar == 'top' and z == 1):
            
        import numpy as np
        data = np.zeros((144,5))
        i = 0
        j = 0
        
        with open('../ValidationData/Sierra_LC1_top.rpt') as f:
            lines = f.readlines()
            fileData = lines[15:159]
            
            for line in fileData:
                
                splitData = line.split(' ')
                
                for k in range(len(splitData)):
                    
                    try: 
                        temp = float(splitData[k])
                        data[i,j] = temp
                        j += 1
        
                    except:
                        temp = 0
                        
                i += 1
                j = 0
                
    elif (spar == 'top' and z == 2):
            
        import numpy as np
        data = np.zeros((144,5))
        i = 0
        j = 0
        
        with open('../ValidationData/Sierra_LC1_top.rpt') as f:
            lines = f.readlines()
            fileData = lines[169:313]
            
            for line in fileData:
                
                splitData = line.split(' ')
                
                for k in range(len(splitData)):
                    
                    try: 
                        temp = float(splitData[k])
                        data[i,j] = temp
                        j += 1
        
                    except:
                        temp = 0
                        
                i += 1
                j = 0
                
    elif (spar == 'front' and z == 1):
        
        import numpy as np
        data = np.zeros((144,5))
        i = 0
        j = 0
        
        with open('../ValidationData/Sierra_LC1_front.rpt') as f:
            lines = f.readlines()
            fileData = lines[15:159]
            
            for line in fileData:
                
                splitData = line.split(' ')
                
                for k in range(len(splitData)):
                    
                    try: 
                        temp = float(splitData[k])
                        data[i,j] = temp
                        j += 1
        
                    except:
                        temp = 0
                        
                i += 1
                j = 0
    elif (spar == 'front' and z == 2):
        
        import numpy as np
        data = np.zeros((144,5))
        i = 0
        j = 0
        
        with open('../ValidationData/Sierra_LC1_front.rpt') as f:
            lines = f.readlines()
            fileData = lines[169:313]
            
            for line in fileData:
                
                splitData = line.split(' ')
                
                for k in range(len(splitData)):
                    
                    try: 
                        temp = float(splitData[k])
                        data[i,j] = temp
                        j += 1
        
                    except:
                        temp = 0
                        
                i += 1
                j = 0
    else:
        data = 0
    
    return data