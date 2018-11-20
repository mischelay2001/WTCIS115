__author__ = 'bb343'

# Write a program for customers to choose lunch combo items.
# Define and use the following three functions:
    #choose_sandwich: Display sandwiches and get user choice
    #choose_side: Display side items and get user choice
    #choose_drink: Display drinks and get user choice
# Each of these functions returns the price of the chosen item.
# Calculate and display the total price in the main function.

def info_to_user():
    # Information to the user
    print()
    print()
    print("Lunch combos in a caf'e include sandwich, side item and a drink.")
    print()
    print("             MENU")
    print()
    print("             SANDWICHES")
    print()
    print("1    Grilled cheese sandwich      $3.00")
    print("2    Chicken sandwich             $3.50")
    print("3    Turkey sandwich              $4.00")
    print()
    print("             SIDES")
    print()
    print("1    French fries                 $1.50")
    print("2    Mashed potato                $1.50")
    print("3    Green beans                  $1.25")
    print("4    Garden salad                 $2.00")
    print()
    print("             BEVERAGES")
    print()
    print("1    Coffee                       $1.25")
    print("2    Iced tea                     $1.00")
    print("3    Soda                         $1.00")
    print()

def choose_sandwich():
    global Sandwich
    global SandwichCost
    Sandwich = input("Enter your sandwich selection i.e. 1, 2, or 3")
    aValidChoice = False
    aVariableDigit = Sandwich.isdigit()
    if Sandwich == "1" or Sandwich == "2" or Sandwich == "3":
        aValidChoice = True
    while aVariableDigit == False or aValidChoice == False:
        print('Your sandwich selection is invalid.')
        try:
            Sandwich = input("Enter your sandwich selection i.e. 1, 2, or 3")
            #Reset Boolean test
            aVariableDigit = Sandwich.isdigit()
            if Sandwich == "1" or Sandwich == "2" or Sandwich == "3":
                aValidChoice = True
        #Program fails if input is alpha or alphanumberic
        #Except if the user's input breaks the code
        except:
            pass
    if Sandwich == "1":
        SandwichCost = 3.00
        print("You have selected grilled cheese sandwich as your sandwich.")
    if Sandwich == "2":
        SandwichCost = 3.50
        print("You have selected chicken sandwich as your sandwich.")
    if Sandwich == "3":
        SandwichCost = 4.00
        print("You have selected turkey sandwich as your sandwich.")
    print()

def choose_side():
    global Side
    global SideCost
    Side = input("Enter your side selection i.e. 1, 2, 3, or 4")
    aValidChoice = False
    aVariableDigit = Side.isdigit()
    if Side == "1" or Side == "2" or Side == "3" or Side == "4":
        aValidChoice = True
    while aVariableDigit == False or aValidChoice == False:
        print('Your side selection is invalid.')
        Side = input("Enter your side selection i.e. 1, 2, 3, or 4")
        #Reset Boolean test
        aVariableDigit = Side.isdigit()
        if Side == "1" or Side == "2" or Side == "3" or Side == "4":
            aValidChoice = True
    if Side == "1":
        SideCost = 1.50
        print("You have selected French fries as your side.")
    if Side == "2":
        SideCost = 1.50
        print("You have selected mashed potatoes as your side.")
    if Side == "3":
        SideCost = 1.25
        print("You have selected green beans as your side.")
    if Side == "4":
        SideCost = 2.00
        print("You have selected garden salad as your side.")
    print()
            
def choose_beverage():
    global Beverage
    global BeverageCost
    Beverage = input("Enter your beverage selection i.e. 1, 2, or 3")
    aValidChoice = False
    aVariableDigit = Beverage.isdigit()
    if Beverage == "1" or Beverage == "2" or Beverage == "3":
        aValidChoice = True
    while aVariableDigit == False or aValidChoice == False:
        print('Your beverage selection is invalid.')
        try:
            Beverage = input("Enter your beverage selection i.e. 1, 2, or 3")
            #Reset Boolean test
            aVariableDigit = Beverage.isdigit()
            if Beverage == "1" or Beverage == "2" or Beverage == "3":
                aValidChoice = True
        #Program fails if input is alpha or alphanumberic
        #Except if the user's input breaks the code
        except:
            pass
    if Beverage == "1":
        BeverageCost = 1.25
        print("You have selected coffee as your beverage.")
    if Beverage == "2":
        BeverageCost = 1.00
        print("You have selected iced tea as your beverage.")
    if Beverage == "3":
        BeverageCost = 1.00
        print("You have selected soda as your beverage.")
    print()

def comboCost():
    global Cost
    Cost = SandwichCost + SideCost + BeverageCost
    print('The cost of your combo is $' + (format(Cost, ',.2f')))
    print()

def main():
    info_to_user()
    choose_sandwich()
    choose_side()
    choose_beverage()
    comboCost()

main()