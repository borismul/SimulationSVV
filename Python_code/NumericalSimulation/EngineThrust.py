'''
This program calculates the shearforce due to the thrust at an arbitrary point of z.

Input variables: thrust force, local z, length from the root till where the engine is suspended
Output variables: shearforce due to the thrust
Output format: float
'''
def EngineThrust(T,z,l3):
    if(z>0 and z<l3):
        return T
    else:
        return 0