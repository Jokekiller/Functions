#Harry Robinson
#03-01-2015
#Currency program

def currency_details():
    currency_convert_to = input("Enter the currecny you want to convert: ")
    currency_convert_from = input("Enter the currecny you are converting from:")
    amount = float(input("Enter the aount you want to convert: "))
    return currency_convert_to, amount, currency_convert_from
def converting_currency(currency_convert_to, amount, currecny_convert_from):
    if currency_convert_from == '£' and currency_convert_to == '$':
        pound_to_dollar = amount * 1.601
        print("£{0} is ${1:.2f}.".format(amount, pound_to_dollar))
    if currency_convert_from == '£' and currency_convert_to == '€':
        pound_to_euro = amount * 1.229
        print("£{0} is €{1:.2f}.".format(amount, pound_to_euro))
    if currency_convert_from == '€' and currency_convert_to == '£':
        euro_to_pound = amount * 0.814
        print("€{0} is £{1:.2f}.".format(amount, euro_to_pound))
    if currency_convert_from == '€' and currency_convert_to == '$':
        euro_to_dollar = amount * 1.302
        print("€{0} is ${1:.2f}.".format(amount, euro_to_dollar))
    if currency_convert_from == '$' and currency_convert_to == '£':
        dollar_to_pound = amount * 0.625
        print("${0} is £{1:.2f}.".format(amount, dollar_to_pound))
    if currency_convert_from == '$' and currency_convert_to == '€':
        dollar_to_euro= amount * 0.768
        print("${0} is €{1:.2f}.".format(amount, dollar_to_euro))
    return
#main program
currency_convert_to, amount, currency_convert_from = currency_details()
converting_currency(currency_convert_to, amount, currency_convert_from)

