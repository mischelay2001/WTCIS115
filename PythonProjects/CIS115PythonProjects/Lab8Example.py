__author__ = 'Michele'

#An instructor wants to create a short computer quiz for his students.
#There are only two questions in the quiz.
#Write a program to implement this quiz.

def ListEntreeSelection():
    print('Please select from one of the four entree options.')
    print('Option 1:  Enter 1 for Fish and Chips')
    print('Option 2:  Enter 2 for Burger and Fries')
    print('Option 3:  Enter 3 for Chicken and Smashed Potatoes')
    print('Option 4:  Enter 4 for Barbecue Pork')
    print()

def EntreeSelection():
    global Entree
    global EntreeText
    Entree = int(input('Please enter your entree selection.'))
    if Entree == 1:
        print('You have selected Fish and Chips.')
        EntreeText = str('Fish and Chips')
    elif Entree == 2:
        print('You have selected Burger and Fries.')
        EntreeText = str('Burger and Fries')
    elif Entree == 3:
        print('You have selected Chicken and Smashed Potatoes.')
        EntreeText = str('Chicken and Smashed Potatoes')
    elif Entree == 4:
        print('You have selected Barbecue Pork.')
    print()

def ListBeverageSelection():
    print('Please select from one of the three beverage options.')
    print('Option 1:  Enter 1 for Iced Tea')
    print('Option 2:  Enter 2 for Soda')
    print('Option 3:  Enter 3 for Coffee')
    print()

def BeverageSelection():
    global Beverage
    global BeverageText
    Beverage = int(input('Please enter your Beverage selection.'))
    if Beverage == 1:
        print('You have selected Iced Tea.')
        BeverageText = str('Iced Tea')
    elif Beverage == 2:
        print('You have selected Soda.')
        BeverageText = str('Soda')
    elif Beverage == 3:
        print('You have selected Coffee.')
        BeverageText = str('Coffee')
    print()

def Message(EntreeText, BeverageText):
    print('We hope you enjoy your', EntreeText, 'and', BeverageText, '.')

def main():
    ListEntreeSelection()
    EntreeSelection()
    ListBeverageSelection()
    BeverageSelection()
    Message(EntreeText, BeverageText)

main()