#Harry Robinson
#08-12-2914
#Password program

#define functions

def password_details():
    password = str(input("Enter a password"))
    return password
def requirements(password):
    password_length = len.password
    while password_length <= 16 and password_length >= 8:
        print("Password accepted")
        if password_length > 16:
            print("password too long")
        elif password_length < 8:
            print("password too short")
    return password_length, password
def actual_password(password_details, requirements):
    password = password_details
    password_length = requirements(password)
    actual_password(password_details, requirements)
    
#main program
actual_password()

                   
