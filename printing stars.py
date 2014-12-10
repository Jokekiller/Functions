#Harry Robinson
#02-12-2014
#Stars program

row = 0

def star_details():
    number_of_stars = int(input("Enter a number: "))
    return number_of_stars
def number_verification(number_of_stars):
    while number_of_stars %2 ==0:
        print("Number is not odd, please try again")
        number_of_stars = int(input("Enter a number: "))
    return number_of_stars
def printing_stars(number_of_stars):
    space_needed = number_of_stars
    while row in range(number_of_stars):
        print(("{0:^"+str(space_needed)+"}").format("*"*number_of_stars))
        number_of_stars = number_of_stars - 2
#main program
number_of_stars = star_details()
number_of_stars = number_verification(number_of_stars)
printing_stars(number_of_stars)
