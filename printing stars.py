#Harry Robinson
#02-12-2014
#Stars program

def star_details():
    number_of_stars = int(input("Enter a number: "))
    return number_of_stars
def number_verification(number_of_stars):
    while number_of_stars %2 ==0:
        number_of_stars = int(input("Enter a number: "))
        if number_of_stars %2 == 0:
            print("Number is odd")
        else:
            print("number is not odd, try again")
    return number_of_stars
def printing_stars(number_of_stars):
    for row in range(number_of_stars):
        number_of_stars = number_of_stars - 2
        print("*"* number_of_stars)
#main program
number_of_stars = star_details()
printing_stars(number_of_stars)
