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
liftDist = 193*10**3*g #(N)
T = 64*10**3*g #(N)

#Defining own input variables
dz = 1

#Importing Python definitions
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#Importing own definitions
import Centroid.Centroid as Centroid
import ChordLength.ChordLength as ChordLength
import EngineWeight.EngineWeight as EngineWeight
import Lift.Lift as Lift
import Moment.Momentx as Momentx
import Moment.Momenty as Momenty
import MomentOfInertia.Ixx as defIxx
import MomentOfInertia.Ixy as defIxy
import MomentOfInertia.Iyy as defIyy
import NormalStress.NormalStress as NormalStress
import NumInt.NumInt as NumInt
import ShearCenter.ShearCenter as ShearCenter
import ShearFlow.ShearFlow as ShearFlow
import ShearForce.ShearForce as ShearForce
import ShearStress.ShearStress as ShearStress
import Torque.Torque as Torque

for z in np.arange(l1+l2+dz,dz):
    chord = ChordLength(cr,ct,l1,l2,z)
    centroid = Centroid(tFront,tRear,tTop,tBottom,chord)
    Ixx = defIxx(tFront,tRear,tTop,tBottom,chord,centroid)
    Ixy = defIxy(tFront,tRear,tTop,tBottom,chord,centroid)
    Iyy = defIyy(tFront,tRear,tTop,tBottom,chord,centroid)
    shearCenter = ShearCenter(tFront,tRear,tTop,tBottom, Ixx,Ixy,Iyy,c)
    lift = Lift(chord,liftDist)
    engineWeight = EngineWeight(me,g)
    shearForce = ShearForce(lift,engineWeight)
    shearFlow = ShearFlow(T,chord,shearForce,shearCenter)
    momentx = Momentx()
    shearStress = ShearStress(shearFlow,tFront,tRear,tTop,tBottom)