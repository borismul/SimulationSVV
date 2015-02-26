import os
clear = lambda: os.system('cls')
clear()

#Importing Python definitions
import numpy as np
import matplotlib.pyplot as plt

#Importing own definitions
from Centroid import Centroid
from ChordLength import ChordLength
from EngineWeight import EngineWeight
from Lift import Lift
from Moment import Moment
from MomentOfInertia import MomentOfInertia
from NormalStress import NormalStress
from PlotImportantGraphs import PlotImportantGraphs
from PlotUnitTests import PlotUnitTests
from ShearCenter import ShearCenter
from ShearStress import ShearStress
from ShearFlow import ShearFlow
from ShearForce import ShearForce
from Torque import Torque
from XYCoordinates import XYCoordinates
from FuelWeight import FuelWeight
from ValidationData import ValidationData


plt.close("all")

#Defining given input variables
cr = 6.27 #(m)
ct = 1.69 #(m)
sweep = -32.2 #(degree)
l1 = 2.88 #(m)
l2 = 27.22 #(m)
l3 = 9.7 #(m)
h3 = 2.14 #(m)
me = 5765 #(kg)
tFront = 0.005 #(-)
tRear = 0.003 #(-)5
tTop = 0.002 #(-)
tBottom = 0.002 #(-)
g = 9.81 #(m/s^2)
liftDist = 193*10**3*g/2 #(N)
T = 64*10**3 #(N)
fuelLiters = 7500 # (liters)
fuelDensity = 0.81 # (kg/liter)

#Defining own input variables
stepsXY = 10
stepsZ = 1000
dz = (l1+l2)/stepsZ
i = stepsZ - 1
moment = [0,0]
lift = 0

#Creating arrays with zeros
shearStressArray = np.zeros((stepsZ,4,stepsXY))
normalStressArray = np.zeros((stepsZ,4,stepsXY))
momentArray = np.zeros((stepsZ,2))
liftArray = np.zeros((stepsZ,1))
shearForceArray = np.zeros((stepsZ,2))
IArray = np.zeros((stepsZ,3))
torqueArray = np.zeros((stepsZ,1))

#Looping through all cross-sections with stepsize dz
for z in reversed(np.linspace(0,l1+l2,num = stepsZ, endpoint = True)):
    
    #Determining chord length, centroid and section ditribution at current cross-Section
    chord = ChordLength(cr,ct,l1,l2,z)
    centroid = Centroid(tFront,tRear,tTop,tBottom,chord)
    coordinates = XYCoordinates(chord,stepsXY,centroid)
    
    #Determining moment of inertia for shear and normal stress and storing it in array
    I = MomentOfInertia(tFront,tRear,tTop,tBottom,chord,centroid)
    IArray[i]= I
    
    # determining Lift for shear force distribution and storing in array
    lift = Lift(z,liftDist,l1,l2,cr,ct,chord,lift,dz)
    liftArray[i] = lift
    
    #determining engineWeight for shear force
    engineWeight = EngineWeight(me,g,z,l3)
    
    #determining engineWeight for shear force
    fuelWeight = FuelWeight(l1,z,fuelLiters,fuelDensity,g)
    
    #determining shearForce for moment distribution and shearflow, storing in array
    shearForce = ShearForce(lift, engineWeight, T, l1, l2, l3, z, fuelWeight)
    shearForceArray[i] = shearForce
    
    #determining moment in the wingbox to be able to calculate the normal stresses and storing in array
    moment = Moment(shearForce,moment,dz)
    momentArray[i] = moment
    
    #deteriming the shearflow and Torque for shear stress calculation
    torque = Torque(lift,engineWeight,fuelWeight,shearForce, moment,coordinates,centroid,chord,z,sweep,l1,l2,l3,h3)
    torqueArray[i] = torque
    shearFlow = ShearFlow(chord, shearForce, torque, I, coordinates,tFront,tTop,tRear,tBottom,False,sweep)
    
    #determining coordinate distribution for the four wingbox sides to be able to calculate the shearflows
    coordinates = XYCoordinates(chord,stepsXY,centroid)    
    
    #Calculating output (shearstress and normalstress)
    shearStress = ShearStress(shearFlow,tFront,tRear,tTop,tBottom)
    normalStress = NormalStress(moment,I,chord,stepsXY,centroid)

    #Storing outputs in 4D/3D array
    shearStressArray[i,:,:] = shearStress
    normalStressArray[i,:,:] = normalStress
    
    #incrementing i with 1 every loop
    i -= 1
    
maxshear = np.amax(shearStressArray, axis = 2)
minshear = np.amin(shearStressArray, axis = 2)

#label = str(chord)
#plt.figure()
#for i in range(4):
#    if i%2 == 0:
#        plt.subplot(221+i)
#        plt.plot(coordinates[1,:],shearStress[i,:], label = label)
#    else:
#        plt.subplot(221+i)
#        plt.plot(coordinates[4,:],shearStress[i,:], label = label)
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0.)
#
#plt.figure()
#for i in range(4):
#    plt.subplot(221+i)
#    plt.plot(range(stepsZ),maxshear[:,i],"b")
#    plt.plot(range(stepsZ),minshear[:,i],"r")

#PlotImportantGraphs(stepsZ,l1,l2,shearForceArray,momentArray,normalStressArray,plt)
PlotUnitTests(stepsZ,l1,l2,IArray,liftArray,coordinates,normalStressArray,torqueArray,plt)
#ValidationData(normalStressArray,shearStressArray,l1,l2,stepsZ,stepsXY)
