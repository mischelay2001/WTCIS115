__author__ = 'Michele Johnson'


# Write a program to play the rock-paper-scissors game.
# A single player is playing against the computer.
# In the main function, ask the user to choose rock, paper or scissors.
# Then randomly pick a choice for the computer.
# Pass the choices of the player and the computer to a find_winner function,
# which determines and displays the outcome of the game.

# Imported Modules
import random

def InfoToUser():
    # Information to the user
    print('Welcome to Rock Paper Scissors!!!')
    print()
    print('This is a single player game against the computer.')
    print('The player will select a weapon from the list below.')
    print('The computer will then select a weapon.')
    print('The most powerful weapon WINS!!!')
    print()
    print('           Weapons List')
    print()
    print('Weapon Code          Weapon')
    print('R                    Rock')
    print('P                    Paper')
    print('S                    Scissors')
    print()
    print()


def GetPlayer1():
    ##User enters input
    global Player1
    Player1 = input('Player 1, please enter your weapon of choice from the list above: ')
    print()
    Player1 = Player1.upper()
    if Player1 != "R" and Player1 != "P" and Player1 != "S":
        print('The player did not enter a valid weapon from the list above.')
    else:
        if Player1 == "R":
            print("The Player's weapon of choice is Rock.")
        if Player1 == "P":
            print("The Player's weapon of choice is Paper.")
        if Player1 == "S":
            print("The Player's weapon of choice is Scissors.")

def GetComputer():
    # Randomly select either R, P, or S
    global Computer
    Computer = ["R", "P", "S"]
    Computer = random.choice(Computer)
    if Computer == "R":
        print("The Computer's weapon of choice is Rock.")
    elif Computer == "P":
        print("The Computer's weapon of choice is Paper.")
    elif Computer == "S":
        print("The Computer's weapon of choice is Scissors.")

def DetermineWinner(Player1, Computer):
    if Player1 == Computer:
        print("It's a Tie!!!")
    elif Player1 == "R" and Computer == "S":
        print("Rock beats Scissors.  Player 1 Wins!!!")
    elif Player1 == "S" and Computer == "P":
        print("Scissors beat Paper.  Player 1 Wins!!!")
    elif Player1 == "P" and Computer == "R":
        print("Paper beats Rocks.  Player 1 Wins!!!")
    elif Computer == "R" and Player1 == "S":
        print("Rock beats Scissors.  The Computer Wins!!!")
    elif Computer == "S" and Player1 == "P":
        print("Scissors beat Paper.  The Computer Wins!!!")
    else:
        print("Paper beats Rocks.  The Computer Wins!!!")

def main():
    # Call Functions
    InfoToUser()
    GetPlayer1()
    GetComputer()
    print()
    DetermineWinner(Player1,Computer)

main()
