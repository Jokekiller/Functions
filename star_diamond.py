#Harry Robinson
#15-12-2014
#Star diamond

row = 0

def star_details():
    number = int(input("Enter a number: "))
    return number
def verification(number):
    valid = False
    if number %2 == 1:
        print("Number OK")
        valid = True
    else:
        print("Number not cool")
    return valid
def printing_stars(number):
    space_needed = (number - 1)/2
    while row in range(number):
         print(("{0:^"+ str(space_needed) + "}").format("*" * number))
         number = number + 2
    while row in range(number):
        print(("{0:^"+ str(space_needed) + "}").format("*" * number))
        number = number - 2

#main program
number = star_details()
valid = verification(number)
printing_stars(number)
