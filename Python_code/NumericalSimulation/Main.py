
#Importing Python definitions
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sys

#Importing own definitions
from Centroid import Centroid
from ChordLength import ChordLength
from EngineWeight import EngineWeight
from Lift import Lift
from Moment import Moment
from MomentOfInertia import MomentOfInertia
from NormalStress import NormalStress
from ShearCenter import ShearCenter
from ShearFlow import ShearFlow
from ShearForce import ShearForce
from ShearStress import ShearStress
from Torque import Torque
from XYCoordinates import XYCoordinates

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
tRear = 0.003 #(-)
tTop = 0.002 #(-)
tBottom = 0.002 #(-)
g = 9.81 #(m/s^2)
liftDist = 193*10**3*g/2 #(N)
T = 64*10**3 #(N)
fuelliters = 7500 # (liters)
fueldensity = 0.81 # (kg/liter)

#Defining own input variables
stepsXY = 1000
stepsZ = 50
dz = (l1+l2)/stepsZ
i = stepsZ - 1
moment = 0
lift = 0

#Creating arrays with zeros
shearStressArray = np.zeros((stepsZ,4,2,stepsXY))
normalStressArray = np.zeros((stepsZ,4,stepsXY))

#Looping through all cross-sections with stepsize dz
for z in reversed(np.linspace(0,l1+l2,num = stepsZ, endpoint = True)):
    
    #Determining variables needed for shear stress and normal stress
    chord = ChordLength(cr,ct,l1,l2,z)
    centroid = Centroid(tFront,tRear,tTop,tBottom,chord)
    I = MomentOfInertia(tFront,tRear,tTop,tBottom,chord,centroid)
    shearCenter = ShearCenter(tFront,tRear,tTop,tBottom,I,chord)
    lift = Lift(z,liftDist,l1,l2,cr,ct,chord,lift,dz)
    engineWeight = EngineWeight(me,g,z,l3)
    
    shearForce = ShearForce(lift, engineWeight, T, fuelliters, fueldensity, l1, l2, l3, z, g)
#    shearFlow = ShearFlow(chord, shearForce, shearCenter, I, stepsXY,centroid,tFront,tTop,tRear,tBottom,False)
    
    torque = Torque(T,h3,chord,shearForce)
    moment = Moment(shearForce,moment,dz)
    #Calculating output (shearstress and normalstress)
#    shearStress = ShearStress(shearFlow,tFront,tRear,tTop,tBottom)
    normalStress = NormalStress(moment,I,chord,stepsXY,centroid)
    print moment
    #Storing in 4D array
#    shearStressArray[i,:,:,:] = shearStress
    normalStressArray[i,:,:] = normalStress
    
    #incrementing i with 1 every loop
    i -= 1
    
maximum = np.amax(normalStressArray, axis = 2)
minimum = np.amin(normalStressArray, axis = 2)

maximum = np.amax(maximum, axis = 1)
minimum = np.amin(minimum, axis = 1)

#plt.plot(range(stepsZ),shearForce)

plt.figure()
for i in range(4):
    plt.plot(range(stepsZ),maximum,"b")
    plt.plot(range(stepsZ),minimum,"r")


plt.figure()
for i in range(2):
    chord = ChordLength(cr,ct,l1,l2,0)
    coordinates = XYCoordinates(chord,stepsXY,centroid)
    plt.plot(coordinates[i*2+1,:],normalStressArray[stepsZ-2,i,:])

plt.xlabel("y (m) -->")
plt.ylabel("sigma (Pa) -->")
plt.figure()
for i in range(2,4):
    chord = ChordLength(cr,ct,l1,l2,0)
    coordinates = XYCoordinates(chord,stepsXY,centroid)
    plt.plot(coordinates[i*2,:],normalStressArray[stepsZ-2,i,:])
plt.xlabel("x (m) -->")
plt.ylabel("sigma (Pa) -->")
