__author__ = 'Michele Johnson'


# Write a program to do the following.
# Generate a random floating number between 12.5 and 17.5.
# Calculate the square root of the random number.
# Display both the random number and its square root.


# Information to the user
print()
print()
print('This program will generate the square root of any random number between 12.5 and 17.5.')
print()
print()

# Calculate Square Root
global cRanNbr
global cSqRt
import random
cRanNbr = random.uniform(12.5,17.5)
import math
cSqRt = math.sqrt(cRanNbr)
print ("The square root of", cRanNbr, "is", cSqRt, '.')

