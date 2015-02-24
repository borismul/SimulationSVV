'''
This program calculates the Moment due to the total shearforce at an arbitrary point of z.

Input variables: shear force, moment at the last z, stepsize in z
Output variables: shearforce due to the lift
Output format: float
'''
def Moment(shearForce,prevMoment,dz):
    #calculate the difference in moment between the sections
    diff = np.multiply(shearForce,dz)
    #Reverse the order of the difference vector, because Sx causes a moment My and vice versa
    diff_reversed = diff[::-1]
    #add the difference to the previous value
    moment = prevMoment + diff_reversed
    return moment

# Unit test
import numpy as np
prevMoment = [1.,1.]
shearForce = [1.,1.]
dz = 1.
if Moment(shearForce,prevMoment,dz) == [2.,2.]