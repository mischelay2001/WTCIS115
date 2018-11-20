__author__ = 'Michele Johnson'

# Write a program to do the following.
# Ask the user to enter a vowel (i.e. 'a', 'e', 'i', 'o' or 'u')
# If it is not a vowel, ask the user to reenter until a vowel is entered.
# Define and use the following function:
# is_not_vowel: test whether is letter is not a vowel.
# Return True if the letter is not a vowel.
# Return False if the letter is a vowel.
# In the main function, ask the user to enter a vowel.
# Pass the letter to the is_not_vowel function to test whether it is a vowel or not.
# Repeat this until a vowel is entered.  Display the vowel entered by the user.

def info_to_user():
    # Information to the user
    print()
    print()
    print('This program takes input from a user and tests if the input is a vowel.')
    print()
    print()

def get_user_input():
    #User enters input
    global cUserInput
    global cValidVowel
    cUserInput = input("Enter a vowel i.e. 'a', 'e', 'i', 'o' or 'u': ")
    print()
    cUserInput = cUserInput.lower()
    if cUserInput != "a" and cUserInput != "e" and cUserInput != "i" and cUserInput != "o" and cUserInput != "u":
        cValidVowel = False
        print("Invalid entry.  Please enter on of the following: 'a', 'e', 'i', 'o' or 'u': ")
    else:
        cValidVowel = True
        print('The user has choosen the vowel', cUserInput, '.')

def main():
    #Call Functions
    info_to_user()
    get_user_input()
    while cValidVowel == False:
        get_user_input()
    print()

main()
