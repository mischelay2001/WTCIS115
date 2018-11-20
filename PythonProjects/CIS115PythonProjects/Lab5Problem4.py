__author__ = 'Michele'
#Information to the user
print('This program calculates the water bill amounts for both residential and business customers.')

##User enters input
print()
print()
print("Will this be for a residential or business customer?")
CustomerType = input('Please type "R" for residential or "B" for business.  ')
CustomerType= CustomerType.upper()

##Learn what type of date the user entered

##Input is made up of only letters; aVariable is alpha - True or False
aVariableAlpha = CustomerType.isalpha()
#print(aVariableAlpha)
##Input is made up of only numbers; aVariable is digit - True or False
aVariableDigit = CustomerType.isdigit()
#print(aVariableDigit)
##Input is made up numbers and letters; aVariable is alphanumber - True or False
aVariableAlphaNumberic = CustomerType.isalnum()
#print(aVariableAlphaNumberic)

ValidCode = CustomerType == "R" or CustomerType == "B"

#Handle invalid user input
#while REQUIRED INPUT DOES NOT MEET NEEDS == False:
while aVariableAlpha == False or ValidCode == False:
            print('Your entry is invalid.')
            try:
                CustomerType = input('Please type "R" for residential or "B" for business.  ')
                CustomerType= CustomerType.upper()
                #Reset Boolean test
                aVariableAlpha = CustomerType.isalpha()
                ValidCode = CustomerType == "R" or CustomerType == "B"
            #Program fails if input is digit or alphanumberic
            #Except if the user's input breaks the code
            except:
                pass

#Handle valid user input:
#while REQUIRED INPUT DOES MEET NEEDS == True:
#Begin program block

if CustomerType == "R":
    GallonsResident = int(input('Enter number of gallons used by customer:  '))
    if GallonsResident >= 8000:
        Difference = GallonsResident - 8000
        Tier1 = (GallonsResident - Difference) * 0.004
        Tier2 = Difference * 0.007
        Bill = Tier1 + Tier2
        print('The customer\'s water bill is $' + (format(Bill, ',.2f')) + '.')
    else:
        Bill = GallonsResident * 0.004
        print('The customer\'s water bill is $' + (format(Bill, ',.2f')) + '.')

else:
    GallonsBusiness = int(input('Enter number of gallons used by customer:  '))
    if GallonsBusiness >= 10000:
        Difference = GallonsBusiness - 10000
        Tier1 = (GallonsBusiness - Difference) * 0.005
        Tier2 = Difference * 0.009
        Bill = Tier1 + Tier2
        print('The customer\'s water bill is $' + (format(Bill, ',.2f')) + '.')
    else:
        Bill = GallonsBusiness * 0.005
        print('The customer\'s water bill is $' + (format(Bill, ',.2f')) + '.')