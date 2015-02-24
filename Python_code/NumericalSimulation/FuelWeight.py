'''
This program calculates the shearforce due to the Fuelweight at an arbitrary point of z.

Input variables: length of the part of the wing where the fuel is located, local z, amount of fuel (liters), fuel density, gravitational accaleration
Output variables: shearforce due to the fuel weight
Output format: float
'''
def FuelWeight(l1,z,fuelLiters,fuelDensity,g):
    if (z>=0 and z<=l1):
        fuelWeight = (l1 - z)/l1 * fuelLiters * fuelDensity * g
        return fuelWeight
    else:
        IOError("z is outside the range")
        return 0

#unit test
l1 = 1.
#test at root, halfway the section where the fuel is, at the end of the fuel and further toward the tip
z = [0,l1/2,l1,l1+1]
fuelLiters = 1
fuelDensity = 1
g = 10
output = []
expectedOutput = [10,5,0,0]
for i in z:
    output.append(FuelWeight(l1,i,fuelLiters,fuelDensity,g))
if output == expectedOutput:
    unit = True
else: unit = False
if unit == False: raise IOError('unit test FuelWeight False')