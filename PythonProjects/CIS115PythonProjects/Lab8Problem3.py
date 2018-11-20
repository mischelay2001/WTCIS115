__author__ = 'Michele Johnson'

# Write a program to convert kilometers to miles.
# Define a function convert_to_miles to convert distance from kilometers to miles with the following formula:

# miles = kilometers x 0.6214

# This function does not get any input from the user directly.
# Instead, the distance in kilometers is passed to this function when it is called.
# In the main function, ask the user to enter a distance in kilometers.
# Pass it to convert_to_miles as an argument.

def MilesToKilometers(Kilometers):
    global Miles
    Miles = Kilometers * 0.6214
    print(Kilometers, "kilometers =", Miles, 'miles.')

def main():
    print('This program converts kilometers into miles.')
    print()
    global Kilometers
    Kilometers = float(input('Please enter the number kilometers to be converted.'))
    MilesToKilometers(Kilometers)

main()