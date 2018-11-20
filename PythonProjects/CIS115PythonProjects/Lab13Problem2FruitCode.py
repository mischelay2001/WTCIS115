__author__ = 'Michele Johnson'
# Write a program to do the following:

# (a)	Ask the user to enter the 4-digit code of an orange.
# (b)	Strip all the leading and trailing whitespace characters from the code.
# (c)	Test whether the code consists of only numeric digits.
# If it is not, display an error message.
# (d)	Test whether the code has exactly 4 characters.
# If it has more or fewer than 4 characters, display an error message.
# (e)	Test the rightmost digit.
# If it is '4', display 'This orange is from California'.
# If it is '7', display 'This orange is from Florida'.
# If it is something else, display 'The last digit must be 4 or 7'.

print()
print()
print("This program will advise the state of origin for an orange.")
print("Please note: For oranges, the last of the 4 digits must be either a '4' or '7'.")
print()
fruitCode = input("Please enter the 4-digit code found on the fruit item:  ")
fruitCode = fruitCode.lstrip()
fruitCode = fruitCode.rstrip()
print()
if fruitCode.isdigit() != True:
    print("The input is invalid.  Please enter exactly four digits.")
    print()
lenFruitCode = len(fruitCode)
if lenFruitCode != 4:
    print("The input is invalid.  Please enter exactly four digits.")
    print()
lastFruitCodeDigit = fruitCode[lenFruitCode-1:]
if lastFruitCodeDigit != '4' and lastFruitCodeDigit != '7':
    print("The input is invalid.  The last of the 4 digits must be either a '4' or '7'.")
if lastFruitCodeDigit == '4':
    print("This code reveals the orange is from Florida.")
else:
    print("This code reveals the orange is from California.")