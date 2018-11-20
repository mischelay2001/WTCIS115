__author__ = 'Michele Johnson'

# Write a program to convert US dollar to Japanese yen.
# This program has two functions: main and convert_to_yen.

def Convert(USDollar, ConvertToYen):
    Yen = USDollar * ConvertToYen
    print('$' + (format(USDollar, ',.2f')) + ' US Dollars would equal $' + (format(Yen, ',.2f')) + ' yen.')
   # print('Your in-state tuition is $' + (format(Tuition, ',.2f')) + '.')

def main():
    global USDollar
    global ConvertToYen
    USDollar = float(input('Enter the US dollars to be converted.'))
    ConvertToYen = float(input('Enter the US to Yen conversion rate.'))
    Convert(USDollar,ConvertToYen)

main()
