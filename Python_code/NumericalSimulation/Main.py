#Importing Python definitions
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sys

#Importing own definitions
import Centroid.Centroid as Centroid
import ChordLength.ChordLength as ChordLength
import EngineWeight.EngineWeight as EngineWeight
import Lift.Lift as Lift
import Moment.Moment as Moment
import MomentOfInertia.I as defI
import NormalStress.NormalStress as NormalStress
import ShearCenter.ShearCenter as ShearCenter
import ShearFlow.ShearFlow as ShearFlow
import ShearForce.ShearForce as ShearForce
import ShearStress.ShearStress as ShearStress
import Torque.Torque as Torque

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
T = 64*10**3*g #(N)

#Defining own input variables
stepsXY = 100
stepsZ = 100
dz = (l1+l2)/stepsZ
i = 0

#Creating 4D arrays with zeros
shearStressArray = np.zeros(stepsZ,stepsZ,stepsXY,stepsXY,4,stepsXY,stepsXY)
normalStressArray = np.zeros(stepsZ,stepsZ,stepsXY,stepsXY,4,stepsXY)

#Looping through all cross-sections with stepsize dz
for z in np.arange(0,l1+l2+dz,dz):
    
    #Determining variables needed for shear stress and normal stress
    chord = ChordLength(cr,ct,l1,l2,z)
    centroid = Centroid(tFront,tRear,tTop,tBottom,chord)
    I = defI(tFront,tRear,tTop,tBottom,chord,centroid)
    shearCenter = ShearCenter(tFront,tRear,tTop,tBottom,I,chord)
    lift = Lift(chord,liftDist)
    engineWeight = EngineWeight(me,g)
    shearForce = ShearForce(lift,engineWeight)
    shearFlow = ShearFlow(T,chord,shearForce,shearCenter)
    torque = Torque(T,h3,chord,shearForce)
    moment = Moment(torque,l3,shearForce)
    
    #Calculating output (shearstress and normalstress)
    shearStress = ShearStress(shearFlow,tFront,tRear,tTop,tBottom)
    normalStress = NormalStress(moment,I,chord,dz)
    
    #Storing in 4D array
    shearStressArray[i,:,:,:,:,:,:] = shearStress
    print(shearStressArray[i,0,0,0,0,0,0])
    normalStress[i,:,:,:,:,:] = normalStress
    
    #incrementing i with 1 every loop
    i += 1
