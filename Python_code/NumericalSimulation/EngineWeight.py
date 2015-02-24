'''
This program calculates the shearforce due to the engine weight for an arbitrary z location.

Input variables:Engine mass, gravitational accaleration, local z, length from root to the point where the engine is suspended
Output variables: shearforce due to the engine weight
Output format: float
'''
def EngineWeight(mEngine,g,z,l3):
    #Engine weight acts only from the root to l3 (where the engine is suspended)
    if(z>0 and z <= l3):
        engineWeight = mEngine*g
        return engineWeight
    else:
        IOError("z is outside the range")
        return 0

#unit test
mEngine = 1
g = 10
l3 = 1
#test at root, place where engine is suspended and furter towards tip
z = [0,l3,l3+1]
output = []
expectedOutput = [10,10,0]
for i in z:
    output.append(EngineWeight(mEngine,g,i,l3))
if output == expectedOutput:
    unit = True
else: unit = False
if unit == False: IOError('unit test EngineWeight False')