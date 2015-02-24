'''
This program calculates the chordlength at an arbitrary point of z.

Input variables: Root and Tip Chord, lengths of the constant and tapered parts of the wing, local z
Output variables: local chord length
Output format: float
'''
def ChordLength(Croot,Ctip,l1,l2,z):
    #From z=0 to z=l1 the chord is the root chord.
    if (z <= l1 and z >= 0):
        Cz = float(Croot)
        return (Cz)
    #From l1 to l1+l2 the chord changes linearly as a function of z.
    elif (z <= (l1 +l2) and z >= l1):
        Cz = Croot - float(Croot-Ctip)/float(l2) * float(z-l1)
        return (Cz)
    #If z is not within the span of the wingbox, the program gives an error.
    else:
        IOError("z is outside the range")
        return 0

#unit test
Croot = 2
Ctip = 1
l1 = 1
l2 = 1
#test at root, end of constant part, halfway the taper and tip
z = [0,l1,l1+l2/2.,l1+l2]
output = []
expectedOutput = [2,2,1.5,1]
for i in z:
    output.append(ChordLength(Croot,Ctip,l1,l2,i))
if output == expectedOutput:
    unit = True
else: unit = False
if unit == False: raise IOError('unit test ChordLength False')