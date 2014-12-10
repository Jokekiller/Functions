def journeyDetails():
    distance = float(input("Enter the distance in miles: "))
    mpg = float(input("enter the mpg of your vehicle: "))
    fuelPrice = float(input("enter the current price of fuel; "))
    return distance, mpg, fuelPrice
def fuelNeeded(distance, mpg):
    amountOfFuelNeeded = mpg / distance
    litres = amountOfFuelNeeded * 4.55
    return litres
def costOfFuel(litres, fuelPrice):
    totalCostOfFuel = litres * fuelPrice
    return totalCostOfFuel
def actualFuelCost(journeyDetails, totalCostOfFuel):
    journeyDetails = distance, mpg, fuelPrice
    distance, mpg = fuelNeeded
    costOfFuel = fuelNeeded, fuelPrice
    print(totalCostOfFuel)
#main program
    
actualFuelCost()
