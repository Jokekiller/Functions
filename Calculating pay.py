#Harry Robinson
#17-11-2014
#Program calculating pay

def calculateBasicPay (hours,pay):
    basicPay = hours * pay
    return basicPay
def calculateOvertimePay (overTimeHours,overTimePay):
    overTimeHours = overTimeHours - 40
    overTimePay = overTimeHours * (1.5 * overTimePay)
    totalOvertimePay = overTimeHours * overTimePay
    basicPay = 40 * overTimePay
    totalPay = basciPay + totalOvertimePay
    return overTimePay
def workDetails ():
    hours = int(input("Enter the hours worked this week: "))
    pay = float(input("Enter your pay: "))
    return hours, pay
def calculateTotalPay(hours,pay):
    if hours <= 40:
        totalPay = calculateBasicPay(hours,pay)
    else:
        totalPay = calculateOvertimePay(hours,pay)
    return totalPay
def displayTotalPay(totalPay):
    print(totalPay)
def calculatePay():
    hours, pay = workDetails()
    totalPay = calculateTotalPay(hours, pay)
    displayTotalPay(totalPay)
    

    
              

#main program
calculatePay()
