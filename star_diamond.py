#Harry Robinson
#15-12-2014
#Star diamond


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
    space_needed = number
    row = 1
    s = "{0:^" + str(space_needed) + "}"
    while row < number:
        print (s.format('*' * row))
        row = row + 2
    row = number
    while row >= 0:
        print(s.format("*" * row))
        row = row - 2

#main program
number = star_details()
valid = verification(number)
printing_stars(number)
