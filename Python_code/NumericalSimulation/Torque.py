def Torque(lift,engineWeight,fuelWeight,shearForce, moment,coordinates,centroid,chordLength,z,sweep,l1,l2,l3,h3,cr):  
    sweep = -sweep * m.pi/180
    Mx = moment[0]
    Sx = shearForce[0]
    if (z>l3 and z<l1+l2):
        wl = Mx/lift
        xl = wl * m.tan(sweep) + cr*0.25-chordLength*0.25
        Torque = lift*(coordinates[0,0]-xl)
        return Torque
    elif (z >= l1 and z <= l3):
        ww = l3-z
        wl = (Mx+engineWeight*ww)/lift
        xl =  wl * m.tan(sweep) + cr*0.25-chordLength*0.25
        xw = ww * m.tan(sweep) + cr*0.25-chordLength*0.25
        Torque = lift*(coordinates[0,0]-xl) - engineWeight*(coordinates[0,0]-xw) + Sx*h3
        return Torque
    elif (z >= 0 and z <= l1):
        ww = l3-z
        wl = (Mx+engineWeight*ww)/lift#(Mx/Sy+engineWeight/Sy*ww)/(1+engineWeight/Sy)
        xl = (wl-(l1-z)) * m.tan(sweep) + cr*0.25-chordLength*0.25
        xw = (ww-(l1-z)) * m.tan(sweep) + cr*0.25-chordLength*0.25
        Torque = lift*(coordinates[0,0]-xl) - engineWeight*(coordinates[0,0]-xw) - fuelWeight*centroid[0] + Sx*h3
        return Torque
    else:
        return 0

#unit test
import math as m
