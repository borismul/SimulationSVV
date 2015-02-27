'''
This program calculates the shearforce due to the thrust at an arbitrary point of z.

Input variables: thrust force, local z, length from the root till where the engine is suspended
Output variables: shearforce due to the thrust
Output format: float
'''
def EngineThrust(T,z,l3):
    if(z>=0 and z<=l3):
        return T
    else:
        return 0

#unit test
#T = 1
#z = [0,1,2]
#l3 = 1
#output = []
#expectedOutput =[1,1,0]
#for i in z:
#    output.append(EngineThrust(T,i,l3))
#if all(output == expectedOutput):
#    unit = True
#else: unit = False
#if unit == False: raise IOError('unit test EngineThrust False')