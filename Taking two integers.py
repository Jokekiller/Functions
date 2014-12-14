#Harry Robinson
#14-12-2014
#Displaying the larger of two numbers

def number_details():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    return x, y
def sort(x, y):
    if x > y:
        return x,y
    else:
        return y,x
#main
x, y = number_details()
larger, smaller = sort(x, y)
print(smaller, larger)

