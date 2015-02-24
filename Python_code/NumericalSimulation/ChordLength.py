## This program calculates the chordlength at an arbitrary point of z.
def ChordLength(Croot,Ctip,l1,l2,z):
    ## From 0 to l1 it was assumed the chord simply stays the root chord.
    if (z <= l1 and z >= 0):
        Cz = float(Croot)
        return (Cz)
    ## From l1 to l1+l2 the chord changes linearly as a function of z.
    elif (z <= (l1 +l2) and z >= l1):
        Cz = Croot - float(Croot-Ctip)/float(l2) * float(z-l1)
        return (Cz)
    ## If z is not within the span length of the wingbox, it returns 0
    else:
        IOError("z is outside the range")
        return 0

#unit test
#print ChordLength(2,1,1,1,1.5)