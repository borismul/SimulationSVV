def FuelWeight(l1,z,fuelLiters,fuelDensity,g):
    fuelWeight = (l1 - z)/l1 * fuelLiters * fuelDensity * g
    return fuelWeight