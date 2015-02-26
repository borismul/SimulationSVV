def Torque(lift,engineWeight,fuelWeight,shearForce, moment,coordinates,centroid,chordLength,z,sweep,l1,l2,l3,h3,cr,ct):  
    sweep = -sweep * m.pi/180
    Mx = moment[0]
    Sx = shearForce[0]
    sweep4 = sweep + m.atan((cr-ct)/(4*l2)) #quarterchord sweep
    if (z>l3 and z<l1+l2):
        wl = Mx/lift
        xl = wl * m.tan(sweep4)
        Torque = -lift*xl
        return Torque
    elif (z >= l1 and z <= l3):
        ww = l3-z
        wl = (Mx+engineWeight*ww)/lift
        xl = wl * m.tan(sweep4)
        xw = ww * m.tan(sweep4)
        Torque = -lift*xl + engineWeight*xw + Sx*(h3+0.05*chordLength)
        return Torque
    elif (z >= 0 and z <= l1):
        ww = l3-z
        wf = l1-z
        wl = (Mx+engineWeight*ww+fuelWeight*wf)/lift
        xl = (wl-wf) * m.tan(sweep4)
        xf = 0.25*chordLength
        xw = (ww-wf) * m.tan(sweep4)
        Torque = -lift*xl + engineWeight*xw + fuelWeight*xf + Sx*(h3+0.05*chordLength)
        return Torque
    else:
        return 0

#unit test
import math as m
