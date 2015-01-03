#Harry Robinson
#03-01-2015
#Cryptography program

def operation_details():
    shiftValue = int(input("Enter a shift value between 0 and 25: "))
    message = input("Enter you're message: ")
    return shiftValue, message
def message_length(shiftValue):
    if shiftValue >= 0 and shiftValue <= 25:
        print("Number valid")
    else:
        print("Number invalid")
    return 
def shift_manipulation(shiftValue, message):
    zValue = ord('z')
    aValue = ord('a')
    cipher = ''
    for i, c in enumerate(message):
        newOrd = ord(c) + shiftValue
        if newOrd > zValue:
            newOrd = aValue + newOrd - zValue
        cipher = cipher + chr(newOrd)
        print(c + '=' + chr (newOrd))
    return cipher

#main program
shiftValue, message = operation_details()
message_length(shiftValue)
cipher = shift_manipulation(shiftValue, message)
print(message)
print(cipher)

