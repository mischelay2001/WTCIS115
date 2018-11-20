__author__ = 'Michele'

#Information to the user
print('Welcome to Rock Paper Scissors!!!')
print()
print('This is a two player game.')
print('Each player will select a weapon from the list below.')
print('Whichever player selects the more powerful weapon WINS!!!')
print()
print('           Weapons List')
print()
print('Weapon Code          Weapon')
print('R                    Rock')
print('P                    Paper')
print('S                    Scissors')
print()
print()

##User enters input
Player1 = input('Player 1, please enter your weapon of choice from the list above: ')
Player1 = Player1.upper()

##Learn what type of date the user entered

##Input is made up of only letters; aVariable is alpha - True or False
aVariableAlpha = Player1.isalpha()
##Input is made up of only numbers; aVariable is digit - True or False
aVariableDigit = Player1.isdigit()
##Input is made up numbers and letters; aVariable is alphanumber - True or False
aVariableAlphaNumberic = Player1.isalnum()

ValidCodePlayer1 = Player1 == "R" or Player1 == "P" or Player1 == "S"

#Handle invalid user input
#while REQUIRED INPUT DOES NOT MEET NEEDS == False:
while aVariableAlpha == False or ValidCodePlayer1 == False:
            print('Player 1, you have no choosen a valid weapon.')
            try:
                Player1 = input('Please enter your weapon of choice from the list above.')
                Player1 = Player1.upper()
                #Reset Boolean test
                aVariableAlpha = Player1.isalpha()
                ValidCodePlayer1 = Player1 == "R" or Player1 == "P" or Player1 == "S"
            #Program fails if input is alpha or alphanumberic
            #Except if the user's input breaks the code
            except:
                pass

Player2 = input('Player 2, please enter your weapon of choice from the list above: ')
Player2 = Player2.upper()

##Learn what type of date the user entered

##Input is made up of only letters; aVariable is alpha - True or False
bVariableAlpha = Player2.isalpha()
##Input is made up of only numbers; aVariable is digit - True or False
bVariableDigit = Player2.isdigit()
##Input is made up numbers and letters; aVariable is alphanumber - True or False
bVariableAlphaNumberic = Player2.isalnum()

ValidCodePlayer2 = Player2 == "R" or Player2 == "P" or Player2 == "S"

#Handle invalid user input
#while REQUIRED INPUT DOES NOT MEET NEEDS == False:
while bVariableAlpha == False or ValidCodePlayer2 == False:
            print('Player 2, you have no choosen a valid weapon.')
            try:
                Player2 = input('Please enter your weapon of choice from the list above.')
                Player2 = Player2.upper()
                #Reset Boolean test
                bVariableAlpha = Player2.isalpha()
                ValidCodePlayer2 = Player2 == "R" or Player2 == "P" or Player2 == "S"
            #Program fails if input is alpha or alphanumberic
            #Except if the user's input breaks the code
            except:
                pass

##Learn what type of date the user entered

##Input is made up of only letters; aVariable is alpha - True or False
bVariableAlpha = Player2.isalpha()
#print(aVariableAlpha)
##Input is made up of only numbers; aVariable is digit - True or False
bVariableDigit = Player2.isdigit()
#print(aVariableDigit)
##Input is made up numbers and letters; aVariable is alphanumber - True or False
bVariableAlphaNumberic = Player2.isalnum()
#print(aVariableAlphaNumberic)

#Handle valid user input:
#while REQUIRED INPUT DOES MEET NEEDS == True:

#Begin program block
if Player1 == Player2:
    print("It's a Tie!!!")
elif Player1 == "R" and Player2 == "S":
    print("Rock beats Scissors.  Player 1 Wins!!!")
elif Player1 == "S" and Player2 == "P":
    print("Scissors beat Paper.  Player 1 Wins!!!")
elif Player1 == "P" and Player2 == "R":
    print("Paper beats Rocks.  Player 1 Wins!!!")
elif Player2 == "R" and Player1 == "S":
    print("Rock beats Scissors.  Player 2 Wins!!!")
elif Player2 == "S" and Player1 == "P":
    print("Scissors beat Paper.  Player 2 Wins!!!")
else:
    print("Paper beats Rocks.  Player 2 Wins!!!")
    