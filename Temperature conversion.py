#Harry Robinson
#14-12-2014
#Temperature conversion

def temp_details():
    temp = int(input("Enter a temperature: "))
    return temp
def conversion(temp):
    celcius = (temp - 32)*(5/9)
    return celcius
#main
temp = temp_details()
celcius = conversion(temp)
print(celcius)
           
