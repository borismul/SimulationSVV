'''
This program calculates the total shearforce acting on a cross section of the wing box at an arbitrary point of z.

Input variables: Shearforces due to the lift, engine Weight, Thrust and Fuelweight
Output variables: Shear forces in x and y
Output format: [float,float]
'''
def ShearForce(lift, engineWeight, T, fuelWeight):
#Add up all the forces that create the shear force (and give them a direction + or - in x or y)
    S_y = lift - engineWeight - fuelWeight
    S_x =  T
    return [S_x, S_y]

#unit test
lift = 4
engineWeight = 3
fuelWeight = 2
T = 1
output = ShearForce(lift, engineWeight, T, fuelWeight)
expectedOutput = [1,-1] # sum of the forces in their respective directions
if output == expectedOutput:
    unit = True
else: unit = False

if unit == False: raise IOError('unit test ShearForce False')