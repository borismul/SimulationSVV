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
from ShearFlow2 import ShearFlow2
from ShearForce import ShearForce
from Torque import Torque
from Torque2 import Torque2
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
liftDist = 193*10**3*g #(N)
T = 64*10**3 #(N)
fuelLiters = 7500 # (liters)
fuelDensity = 0.81 # (kg/liter)

#Defining own input variables
stepsXY = 10
stepsZ = 10
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
    torque = Torque(lift,engineWeight,fuelWeight,shearForce, moment,coordinates,centroid,chord,z,sweep,l1,l2,l3,h3,cr)
    torqueArray[i] = torque
    shearFlow = ShearFlow(chord, shearForce, torque, I, coordinates,tFront,tTop,tRear,tBottom,False,sweep)
    
    #determining coordinate distribution for the four wingbox sides to be able to calculate the shearflows
    coordinates = XYCoordinates(chord,stepsXY,centroid)    
    
    #Calculating output (shearstress and normalstress)
    shearStress = ShearStress(shearFlow,tFront,tRear,tTop,tBottom)
    normalStress = NormalStress(moment,I,chord,stepsXY,centroid)

    #Storing outputs in 3D array
    shearStressArray[i,:,:] = shearStress
    normalStressArray[i,:,:] = normalStress
    
    #incrementing i with 1 every loop
    i -= 1


PlotImportantGraphs(stepsZ,l1,l2,shearForceArray,momentArray,normalStressArray,shearStressArray,plt)
PlotUnitTests(stepsZ,l1,l2,IArray,liftArray,coordinates,normalStressArray,shearStressArray,torqueArray,plt)
ValidationData(normalStressArray,shearStressArray,l1,l2,stepsZ,stepsXY)
