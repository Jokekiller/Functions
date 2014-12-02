#Harry Robinson
#02-12-2014
#Output symbols

def informtaion_details():
    integer = int(input("Enter a number: "))
    character =input("Enter a character: ")
    return integer, character
def output_symbol(integer, character):
    for count in range(integer):
        print(character, end="")
#main program
integer, character = informtaion_details()
output_symbol(integer, character)        
    
