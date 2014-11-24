#Harry Robinson
#17-11-2014
#Program calculating pay

def calculateBasicPay (hours,pay):
    basicPay = hours*pay
    return basicPay
def calculateOvertimePay (overTimeHours,overTimePay):
    overTimeHours = hours - 40
    overTimePay = overTimeHours * (1.5 * pay)
    totalOvertimePay = overtimeHours * overtimePay
    basicPay = 40 * pay
    totalPay = basciPay + totalOvertimePay
    return overTimePay
def workDetails ():
    hours = int(input("Enter the hours worked this week: "))
    pay = int(input("Enter your pay: "))
def displayTotalPay(totalPay):
    
              

#main program
total = calculateBasicPay(30,5)
print(total)
