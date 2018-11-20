__author__ = 'Michele'
#Information to the user
print('Volume Discount*')
print('*Unit price is dependent on number of copies purchased.')
print('')
print('Number of copies purchased               Unit Price')
print('1 - 10                                   $99')
print('11 - 50                                  $89')
print('51 - 100                                 $79')
print('101 or more                              $69')
print('')

##User enters input
Copies = input('How many copies are you buying?  ')

##Learn what type of date the user entered

##Input is made up of only letters; aVariable is alpha - True or False
aVariableAlpha = Copies.isalpha()
#print(aVariableAlpha)
##Input is made up of only numbers; aVariable is digit - True or False
aVariableDigit = Copies.isdigit()
#print(aVariableDigit)
##Input is made up numbers and letters; aVariable is alphanumber - True or False
aVariableAlphaNumberic = Copies.isalnum()
#print(aVariableAlphaNumberic)

#Handle invalid user input
while aVariableDigit == False:
            print('Your entry is invalid.  Please select a valid code from the table above.')
            try:
                Copies = input('Please enter the number of copies you are buying:  ')
                aVariableDigit = Copies.isdigit()
            #Program fails if input is alpha or alphanumberic
            #Except if the user's input breaks the code
            except:
                pass

#Handle valid user input:
#Program requires input to be a digit
#while aVariableDigit == True:
if aVariableDigit == True:
    #Force input into integer
    Copies = int(Copies)

    #Begin program comparison
    if Copies <=10:
        UnitPrice = 99
        TotalPrice = UnitPrice * Copies
    elif Copies >10 and Copies <=50:
            UnitPrice = 89
            TotalPrice = UnitPrice * Copies
    elif Copies >51 and Copies <=100:
            UnitPrice = 79
            TotalPrice = UnitPrice * Copies
    else:
            UnitPrice = 69
            TotalPrice = UnitPrice * Copies
print('The unit price is $' + format(UnitPrice, ',.0f') + '.  The total price is $' + format(TotalPrice, ',.0f') + '.')
