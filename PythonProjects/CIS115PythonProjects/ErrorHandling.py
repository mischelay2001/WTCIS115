__author__ = 'Michele'
#Information to the user
print('PRINT SOMETHING')

##User enters input
Copies = input('ASK USER FOR INPUT')

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
#while REQUIRED INPUT DOES NOT MEET NEEDS == False:
while aVariableDigit == False:
            print('ERROR MESSAGE.')
            try:
                Copies = input('ASK USER FOR VALID INPUT')
                #Reset Boolean test
                aVariableDigit = Copies.isdigit()
            #Program fails if input is alpha or alphanumberic
            #Except if the user's input breaks the code
            except:
                pass

#Handle valid user input:
#while REQUIRED INPUT DOES MEET NEEDS == True:
if aVariableDigit == True:
    #Force input into integer
    Copies = int(Copies)

    #Begin program block


